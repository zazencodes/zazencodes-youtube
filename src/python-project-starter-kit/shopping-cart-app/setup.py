from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='shopping_cart',
    version='1.1',
    packages=find_packages(),
    install_requires=requirements,
)

