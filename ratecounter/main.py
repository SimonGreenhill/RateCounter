#!/usr/bin/env python3
#coding=utf-8
__author__ = 'Simon J. Greenhill <simon@simon.net.nz>'
__copyright__ = 'Copyright (c) 2017 Simon J. Greenhill'
__license__ = 'New-style BSD'

from nexus import NexusReader
from collections import Counter

class Score(object):
    
    MISSING = ('?', '-', )
    
    def __init__(self, taxonA, taxonB, other):
        self.taxonA = self._check(taxonA)
        self.taxonB = self._check(taxonB)
        self.other = self._check(other)
        self.pattern = (self.taxonA, self.taxonB, self.other)
    
    def __repr__(self):
        return "<Score (%s, %s, %s) = %s>" % (
            self.taxonA, self.taxonB, self.other, self.state
        )
        
    def _check(self, value):
        if value not in ('0', '1', '?', '-'):
            raise ValueError("Unknown state: %s" % value)
        return value
    
    @property
    def state(self):
        #
        #  A --1--|
        #         +----5--+
        #  B --2--|       |
        #                 |-----6
        #                 |
        #  C --3----------+ 
        #
        if any([_ in self.MISSING for _ in self.pattern]):
            return 'UNCOUNTABLE'
        elif self.pattern == ('1', '1', '1'):
            return 'RETENTION'             # 6 = noninformative
        elif self.pattern == ('1', '1', '0'):
            return 'SHARED GAIN'           # 5 = noninformative
        elif self.pattern == ('1', '0', '0'):
            return 'GAIN A'                # +1 = informative
        elif self.pattern == ('0', '1', '0'):
            return 'GAIN B'                # +2 = informative
        elif self.pattern == ('1', '0', '1'):
            return 'LOSS B'                # -2 = informative
        elif self.pattern == ('0', '1', '1'):
            return 'LOSS A'                # -1 = informative
        elif self.pattern == ('0', '0', '1'):
            return 'SHARED LOSS'           # 3,6 = noninformative
        elif self.pattern == ('0', '0', '0'):
            return 'ABSENCE'               # nothing
        else:  # pragma: no cover
            raise ValueError("should not happen")


class RateCounter(object):
    """Rate Counter"""
    PRESENT_STATES = ('1', )
    MISSING_STATES = ('-', '?', )
    ABSENCE_STATES = ('0', )

    KEYLIST = [
        'GAIN A', 'GAIN B',
        'LOSS A', 'LOSS B',
        'TOTAL A', 'TOTAL B',
        'ABSENCE', 'RETENTION',
        'SHARED GAIN', 'SHARED LOSS',
        'UNCOUNTABLE',
        'TOTAL',
    ]

    def __init__(self, matrix=None, nexusfile=None):
        self._nchar = None
        if nexusfile is not None:
            self.matrix = NexusReader(nexusfile).data.matrix
        else:
            self.matrix = matrix

    @property
    def nchar(self):
        if not self._nchar:
            for t in self.matrix:
                if self._nchar is None:
                    self._nchar = len(self.matrix[t])
                if len(self.matrix[t]) != self._nchar:
                    raise ValueError("Site length mismatch")
        return self._nchar
    
    @property
    def taxa(self):
        return self.matrix.keys() if self.matrix else {}
    
    def _get_other(self, site, taxa):
        # get all values for this site in all other taxa not found in `taxa`
        others = [self.matrix[t][site] for t in self.matrix if t not in taxa]
        # return 1 if there is at LEAST one present state in any OTHER taxa
        if len([_ for _ in others if _ in self.PRESENT_STATES]):
            return '1'
        # return ? if ALL other values are missing states
        elif all([_ in self.MISSING_STATES for _ in others]):
            return '?'
        # return 0 if ALL other values are absent or missing states
        elif all([_ in self.ABSENCE_STATES + self.MISSING_STATES for _ in others]):
            return '0'
        # should not happen
        else:  # pragma: no cover
            raise ValueError("Unknown other pattern %r" % others)
    
    def get_scores(self, taxon1, taxon2, explain=False):
        assert taxon1 in self.matrix, "missing taxon: %s" % taxon1
        assert taxon2 in self.matrix, "missing taxon: %s" % taxon2
        scores = Counter({k:0 for k in self.KEYLIST})
        for site in range(self.nchar):
            s = Score(
                self.matrix[taxon1][site],
                self.matrix[taxon2][site],
                self._get_other(site, [taxon1, taxon2])
            )
            if explain:
                print(site + 1, s)
            scores[s.state] += 1
        scores['TOTAL'] = sum(scores.values())
        scores['TOTAL A'] = scores.get('GAIN A', 0) + scores.get('LOSS A', 0)
        scores['TOTAL B'] = scores.get('GAIN B', 0) + scores.get('LOSS B', 0)
        return scores
    
    def display(self, scores):
        for k in self.KEYLIST:
            print("%20s\t%d" % (k, scores.get(k, 0)))
    
