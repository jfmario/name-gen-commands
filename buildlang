#!/usr/bin/env python

import json
import os.path
import sys

from os.path import expanduser

SETTINGSDIR = '.namelangs'

# algorithm borrowed from
# https://towardsdatascience.com/generating-startup-names-with-markov-chains-2a33030a4ac0

def build_markov_chain(data, n=3):
    chain = {
        '_initial':{},
        '_names': set(data)
    }
    for word in data:
        word_wrapped = str(word) + '.'
        for i in range(0, len(word_wrapped) - n):
            tuple = word_wrapped[i:i + n]
            next = word_wrapped[i + 1:i + n + 1]
            
            if tuple not in chain:
                entry = chain[tuple] = {}
            else:
                entry = chain[tuple]
            
            if i == 0:
                if tuple not in chain['_initial']:
                    chain['_initial'][tuple] = 1
                else:
                    chain['_initial'][tuple] += 1
                    
            if next not in entry:
                entry[next] = 1
            else:
                entry[next] += 1

    chain['_names'] = list(chain['_names'])
    return chain  

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print ("Syntax: buildlang [file] [name] [n=3]")
        sys.exit(1)

    with open(sys.argv[1]) as f:

        words = [l.strip() for l in f.readlines() if len(l) > 0]

        n = 3

        if len(sys.argv) > 3:
            n = int(sys.argv[3])

        chain = build_markov_chain(words, n)

        userdir = expanduser('~')

        if not os.path.exists(os.path.join(userdir, SETTINGSDIR)):
            os.makedirs(os.path.join(userdir, SETTINGSDIR))

        with open(os.path.join(userdir, SETTINGSDIR, sys.argv[2]), 'w') as o:
            o.write(json.dumps(chain))

      