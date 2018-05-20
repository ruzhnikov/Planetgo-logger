
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import pgo_logger as planetgo_logger


setup(
    name="planetgo_logger",
    version=planetgo_logger.__version__,
    packages=find_packages(exclude=['tests']),
    author="Alexander Ruzhnikov",
    author_email="ruzhnikov85@gmail.com",
    license="MIT",
    python_requires='>=3',
    description="Planetgo logger",
    long_description="""
        A simple logger for using in other kinds of planetgo site
        """
)
