#!/usr/bin/env python

import json
import os.path
import random
import sys

from os.path import expanduser

SETTINGSDIR = '.namelangs'

# algorithm borrowed from
# https://towardsdatascience.com/generating-startup-names-with-markov-chains-2a33030a4ac0

def select_random_item(items):
    rnd = random.random() * sum(items.values())
    for item in items:
        rnd -= items[item]
        if rnd < 0:
            return item
        
def generate(chain):
    tuple = select_random_item(chain['_initial'])
    result = [tuple]
    
    while True:
        tuple = select_random_item(chain[tuple])
        last_character = tuple[-1]
        if last_character == '.':
            break
        result.append(last_character)
    
    generated = ''.join(result)
    if generated not in chain['_names']:
        return generated
    else:
        return generate(chain)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print ("Syntax: buildlang [name] [n=10]")
        sys.exit(1)

    langname = sys.argv[1]
    n = 10

    if len(sys.argv) > 2:
        n = int(sys.argv[2])

    chainfile = os.path.join(expanduser('~'), SETTINGSDIR, langname)

    if not os.path.exists(chainfile):
        print ("Language %s does not exist." % langname)
        sys.exit(1)

    with open(chainfile) as f:
        chain = json.loads(f.read())

    for i in range(0, n):
        name = generate(chain)
        print (name)