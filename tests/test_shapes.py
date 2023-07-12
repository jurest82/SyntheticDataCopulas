import numpy as np
import pandas as pd
from non_parametric import generate_multivariate_data
import pytest


@pytest.mark.parametrize("n, k, N", [(100, 3, 1000), (1000, 5, 100), (3, 1, 3)])
def test_generated_samples(n, k, N):
    n = 100
    k = 3
    N = 1000
    data = pd.DataFrame(np.random.normal(size=(n, k)), columns=range(k))
    generated_data = generate_multivariate_data(data, N=N)
    assert generated_data.shape == (N, k)
