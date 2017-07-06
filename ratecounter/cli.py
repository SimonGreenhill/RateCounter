#!/usr/bin/env python3
#coding=utf-8
__author__ = 'Simon J. Greenhill <simon@simon.net.nz>'
__copyright__ = 'Copyright (c) 2017 Simon J. Greenhill'
__license__ = 'New-style BSD'

import os
import sys
import argparse

from nexus import NexusReader
from ratecounter.main import RateCounter

def parse_args(*args):
    """
    Parses command line arguments
    
    Returns a tuple of (nexus, taxon1, taxon2)
    """
    descr = 'Calculate rates from the nexus for the two taxa'
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument("nexus", help='nexusfile')
    parser.add_argument("taxon1", help='Taxon 1')
    parser.add_argument("taxon2", help='Taxon 2')
    parser.add_argument(
        '-v', "--verbose", dest='verbose', default=False,
        help="increases verbosity", action='store_true'
    )
    args = parser.parse_args(args)
    return (args.nexus, args.taxon1, args.taxon2, args.verbose)

def main(args=None):
    args = sys.argv[1:] if args is None else args
    nexus, taxon1, taxon2, verbose = parse_args(*args)
    if not os.path.isfile(nexus):
        raise IOError("%s does not exist" % nexus)
    m = RateCounter(NexusReader(nexus).data.matrix)
    m.display(m.get_scores(taxon1, taxon2, explain=verbose))
