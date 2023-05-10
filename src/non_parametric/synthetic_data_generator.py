import numpy as np
import pandas as pd

from .empirical_cumulative_distribution import cdf
from .frequency_table import frequency_table


def generate_multivariate_data(X: pd.DataFrame, bins: int = 10, N: int = 1000):
    """This function generates new multivariate data respecting the dependency
    structures between variables.

    Read the article Restrepo, J.P.; Rivera, J.C.; Laniado, H.; Osorio,
    P.; Becerra, O.A. 
    Nonparametric Generation of Synthetic Data Using Copulas. 
    Electronics 2023, 12, 1601. https://doi.org/10.3390/electronics12071601
    if you have any questions.

    -----------
    Parameters:
    X
      It is the original dataset
    bins
      It is the number of classes of intervals for the calculation
      of the frequency table
    N
      It is the number of simulated data to generate

    -----------
    Returns:
    X_generated: DataFrame
      It is the simulated data"""

    # i) generate matrix of empirical distributions

    matrix_F = X.copy(deep=True)

    for i in matrix_F.columns:
        X_column_i = matrix_F[i]
        x_sort_i, F_i = cdf(X_column_i)
        matrix_F[i] = [F_i[np.where(x_sort_i == z)[0][0]] for z in X_column_i]

    # ii) A frequency table is constructed for each variable with
    # the given number of bins.

    dicc_freq_tables = {}

    for i in X.columns:
        X_column_i = X[i]
        simple_table = frequency_table(X_column_i, bins=bins)
        complete_table = pd.DataFrame.from_dict(
            simple_table, orient="index", columns=["Freq_abs"]
        )
        freq_rel = [j / len(X_column_i) for j in simple_table.values()]
        complete_table["Freq_rel"] = freq_rel
        complete_table["Freq_acum"] = np.cumsum(freq_rel)

        dicc_freq_tables[i] = complete_table

    # iii) - iv)  List of N integers between 0 and n-1

    list_N = np.random.randint(low=0, high=len(matrix_F), size=N)

    # v) - vi)  Simulation

    X_generated = pd.DataFrame(columns=X.columns)

    for sub_n in list_N:
        random_generated = []

        for i in X.columns:
            h = matrix_F.loc[sub_n, i]
            # inverval or freq_table where is the percentile
            interval = next(
                (
                    j
                    for j in range(0, len(dicc_freq_tables[i]["Freq_acum"]))
                    if dicc_freq_tables[i]["Freq_acum"][j] >= (h)
                ),
                None,
            )
            if interval == None:
                interval = -1

            lim_inf = dicc_freq_tables[i].index[interval][0]
            lim_sup = dicc_freq_tables[i].index[interval][1]
            random_generated.append(
                np.random.uniform(low=lim_inf, high=lim_sup, size=1)[0]
            )

        random_generated = np.array(random_generated).T
        random_generated = pd.DataFrame([random_generated], columns=X.columns)
        X_generated = pd.concat([X_generated, random_generated], ignore_index=True)

    return X_generated
