# HEA Express

Welcome to HEA Express - a Python library designed to provide a comprehensive set of AI tools for working with high-entropy alloys! It offers functionalities for data preprocessing, feature extraction, predictive modeling, and analysis of HEA properties.

Developed by Dmitriy Volynov (c) 2024

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)


## Installation

You can install this package in Google Colab using the following commands:

```python
!rm -rf 'heaexpress'
!git clone -q https://github.com/dvolynov/heaexpress.git
!pip install -r heaexpress/requirements.txt
```

## Usage

Here's a quick example of how to vectorize a composition of a stable high-enthropy alloy: 

```python
from heaexpress.encoders import Stable

composition = 'Co1Cr1Fe1Mn1Ni1'
encoder = Stable(density=10)
matrix = encoder.to_matrix(composition)
print(matrix)
```

## Features

- **Data Preprocessing**: clean and prepare your HEA datasets for analysis.
- **Feature Extraction**: extract relevant features from HEA compositions and structures.
- **Predictive Modeling**: train machine learning models to predict various properties of HEAs.
- **Analysis Tools**: analyze model performance and interpret results to gain insights into HEA behavior.

## License 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.