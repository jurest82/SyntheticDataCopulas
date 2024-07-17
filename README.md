# Non-parametric-multivariate-data-generator

This repository contains the code for the Python3 implementation of the method explained in the following article:
Restrepo, J.P.; Rivera, J.C.; Laniado, H.; Osorio, P.; Becerra, O.A. Nonparametric Generation of Synthetic Data Using Copulas. Electronics 2023, 12, 1601. <https://doi.org/10.3390/electronics12071601>

## License

This package is part of this stack will be "source available", not
“open source”, although that will provide nearly all of the openness
that users would typically get from an Apache 2.0 license:

- It provides access to the source code, just like Apache 2.0.
- It provides the ability for users to modify the source code,
just like Apache 2.0.
- It provides the ability for users to run the source code on their own behalf,
just like Apache 2.0.
- It has a very cool provision whereby all code released actually graduates
into true Apache 2.0 open source after a certain period
(we plan to use 3 years).

The main difference between the BSL and Apache 2.0 for the community will be
that recent versions of the the package will not be able to be incorporated
into other commercial products. A user will be able to deploy and use all
versions of the server for themselves / their company just as they would
with Apache 2.0 code.

## Installation

```bash
pip install non-parametric-multivariate-data-generator
```

## Examples of synthetic data generation

The file `example.ipynb` contains five examples of synthetic data generation

## Example usage

```python
import numpy as np
import pandas as pd
data = pd.DataFrame(np.random.normal(size=(100, 3)), columns=['a', 'b', 'c'])

from  non_parametric import generate_multivariate_data
generated_data = generate_multivariate_data(data, N=1000)
generated_data.head()
"""
          a         b         c
0 -0.811318 -2.199115  0.911802
1  1.006849  0.695056  0.027386
2  0.839067 -0.194327 -0.641318
3 -0.955104 -0.384175  0.462385
4 -0.197083  2.520539 -0.835229
"""
```

## Dependecies

To install the dependencies use pip

```
pip install -r requirements.txt
```

The main packages are:

- numpy
- pandas
- matplotlib

## To install, test locally and develop

1. Create and activate a python virtual env
1. `pip install -e ".[dev]"`
1. `pytest`
1. `pre-commit install`

## To install anywhere else

1. Create and activate a python virtual env
1. `python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple non-parametric-multivariate-data-generator`

## To deploy to pypi

1. Create and activate a python virtual env
1. `python3 -m pip install --upgrade pip`
1. `python3 -m pip install --upgrade build`
1. `python3 -m pip install --upgrade twine`
1. Change project version property in `pyproject.toml`
1. `python3 -m build`
1. `python3 -m twine upload --repository testpypi dist/*`
   El usuario es `__token__` y la contraseña se genera en <https://test.pypi.org/manage/account/token/>
