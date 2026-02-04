from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='chanter',

    version='0.1.6',

    description='Simple quiescent galaxy spectral modelling and fitting',

    long_description=long_description,

    author='Struan Stevenson',

    author_email='struan.stevenson@ed.ac.uk',

    packages= find_packages(),

    package_data = {'': ['*.txt', '*.fits'],},  

    install_requires=["numpy", "astropy", "matplotlib", "spectres", "nautilus-sampler"],

)
