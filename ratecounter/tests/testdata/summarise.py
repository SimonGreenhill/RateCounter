#!/usr/bin/env python3
#coding=utf-8
"""
Small script intended to summarise the test data files outside the
ratecounter framework (for setting up test cases only).
"""
from collections import Counter
from nexus import NexusReader

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Does something.')
    parser.add_argument("filename", help='filename')
    args = parser.parse_args()
    
    nex = NexusReader(args.filename)
    patterns = Counter()
    for char_id in nex.data.characters:
        p = "".join([
            nex.data.characters[char_id]['A'],
            nex.data.characters[char_id]['B'],
            nex.data.characters[char_id]['F'],
        ])
        patterns[p] += 1

    for p in patterns.most_common():
        print(p)
    print(sum(patterns.values()))
