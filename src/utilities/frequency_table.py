import matplotlib.pyplot as plt


def frequency_table(data, bins=5):
    '''This function returns a table of frequencies for a given univariate array.

    ----------
    Parameters:
    data: list, numpy array
      It is the list or array of univariate data from which you want to get the 
      frequency table
    bins: int
      It is the desired number of intervals for the frequency table

    ----------
    Returns:
      freq_table: diccionary
      Frequency table of the form:
      freq_table = {tuple([0, 4]): 3, tuple([4, 8]): 5, tuple([8, 12]): 6, 
                         tuple([12, 16]): 4, tuple([16, 20]): 3}
    '''

    ax = plt.hist(data, bins=bins)
    plt.close()
    freqs = ax[0]
    intervals = ax[1]

    freq_table = {}

    for i in range(0, len(intervals)-1):
        freq_table[tuple([intervals[i], intervals[i+1]])] = int(freqs[i])

    return freq_table
