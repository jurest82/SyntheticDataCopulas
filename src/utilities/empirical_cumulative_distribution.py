import numpy as np

def cdf(random_variable):

  '''This function computes the empirical cumulative distribution function 
  of an array named 'random_variable'. Returns 'random_variable' with its 
  unique elements in ascending order and also the distribution function.
  
  -----------
  Parameters:
  random_variable: 1D - array
    The array containing the values of the random variable
    to which the cumulative distribution function will be calculated
  
  -----------
  Returns:
  x: 1D - array
    Unique values of random_variable in ascending order
  cdf: 1D - array
    empirical cumulative distribution function'''

  x, counts = np.unique(random_variable, return_counts=True)
  cusum = np.cumsum(counts)
  cdf = cusum / cusum[-1]
  return x, cdf