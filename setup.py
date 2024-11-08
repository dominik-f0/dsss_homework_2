from distutils.core import setup
from setuptools import find_packages

setup(
    name="Mathquiz",
    version ="0.1",
    author="DB",
    author_email="dominik.baer@fau.de",
    packages=find_packages(),
    install_requires=["numpy", "turtles"]

)