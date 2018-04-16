# RateCounter

[![Build Status](https://travis-ci.org/SimonGreenhill/RateCounter.svg?branch=master)](https://travis-ci.org/SimonGreenhill/RateCounter)
[![Coverage Status](https://coveralls.io/repos/github/SimonGreenhill/RateCounter/badge.svg?branch=master)](https://coveralls.io/github/SimonGreenhill/RateCounter?branch=master)

*RateCounter* is a python library and program for calculating the number of rate differences between taxa given a nexus file. 

It is based on the method in:

```
Greenhill SJ, Hua X, Welsh CF, Schneemann H & Bromham L. 2018. [Population Size and the Rate of Language Evolution: A Test across Indo-European, Austronesian and Bantu Languages](https://www.frontiersin.org/articles/10.3389/fpsyg.2018.00576/abstract). Frontiers in Psychology doi: 10.3389/fpsyg.2018.00576
```

Please cite this paper if you find this software helpful.

**Installation:**

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
