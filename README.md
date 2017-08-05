# RateCounter

[![Build Status](https://travis-ci.org/SimonGreenhill/RateCounter.svg?branch=master)](https://travis-ci.org/SimonGreenhill/RateCounter)
[![codecov](https://codecov.io/gh/SimonGreenhill/RateCounter/branch/master/graph/badge.svg)](https://codecov.io/gh/SimonGreenhill/RateCounter)

*RateCounter* is a python library and program for calculating the number of rate differences between taxa given a nexus file. 

It is based on the method in:

    Bromham L, Hua X, Fitzpatrick T, & Greenhill SJ. 2015. [Rate of language evolution is affected by population size](http://www.pnas.org/content/112/7/2097.abstract). Proceedings of the National Academy of Sciences, USA. 
  
**Installation**

```shell
pip install ratecounter
```

**Usage:**

As a standalone program:

```shell
> ratecounter --help

usage: ratecounter [-h] [-v] nexus taxon1 taxon2

Calculate rates from the nexus for the two taxa

positional arguments:
  nexus          nexusfile
  taxon1         Taxon 1
  taxon2         Taxon 2

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increases verbosity


> ratecounter test.nex Taxon1 Taxon2
              GAIN A	1
              GAIN B	1
              LOSS A	1
              LOSS B	1
             TOTAL A	2
             TOTAL B	2
             ABSENCE	1
           RETENTION	1
         SHARED GAIN	1
         SHARED LOSS	1
         UNCOUNTABLE	19
               TOTAL	27
```

As a python library

```python
from ratecounter.main import RateCounter

rc = RateCounter(nexusfile=args.nexusfile)
scores = rc.get_scores(Taxon1, Taxon2)
```
