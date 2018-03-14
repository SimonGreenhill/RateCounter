#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

from ratecounter import __version__

setup(
    name='RateCounter',
    version=__version__,
    description="ratecounter - Nexus file rate counter for language phylogenies",
    url='',
    author='Simon J. Greenhill',
    author_email='simon@simon.net.nz',
    license='BSD',
    zip_safe=True,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='language-phylogenies',
    packages=find_packages(),
    install_requires=['python-nexus>=1.4',],
    tests_require=['pytest', ],
    entry_points={
        'console_scripts': [
            'ratecounter = ratecounter.cli:main'
        ],
    },
)
