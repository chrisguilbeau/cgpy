from setuptools import find_packages
from setuptools import setup

setup(
    name='cgpy',
    version='0.0.2',
    packages=find_packages(include=['cgpy', 'cgpy.*'])
    )
