from setuptools import find_packages, setup

with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name="non-parametric-multivariate-data-generator",
    version="0.0.1",
    description="A package to generate multivariate data.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jurest82/SyntheticDataCopulas",
    author="Juan P. Restrepo and Pablo Osorio",
    author_email="jurest82@eafit.edu.co, osoriopabl@gmail.com",
    license="Business Source License (BSL)",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas>=1.3.5", "matplotlib>=3.2.2", "numpy>=1.21.6"],
    extras_require={
        "dev": [
            "jupyterlab>=3.2.1",
            "openpyxl==3.0.10",
            "pre-commit>=3.11",
            "pytest>=7.0",
            "scikit-learn==1.0.2",
            "scipy==1.7.3",
            "seaborn==0.11.2",
            "twine>=4.0.2",
        ],
    },
    python_requires=">=3.11",
)
