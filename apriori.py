"""
Each row corresponds to a transaction.
Each row contains space-separated integers. Each integer represents an SKU.

Return all sets of size 3 or more that appear sigma or more times together in a transaction.

APPROACH
apriori algorithm: 
https://en.wikipedia.org/wiki/Apriori_algorithm

very time and memory intensive

count how many times each item occurs
prune those that do not appear at least sigma times

generate a list of all pairs of the frequent counts
prune those that do not appear at least sigma times

generate a list of all sets of 3
prune those that do not appear at least sigma times
"""
import ipdb
from tqdm import tqdm
import itertools


def prune(counts, sigma):
    filtered = set()
    for (k, v) in counts.items():
        if v >= sigma: 
            filtered.add(k)
    return filtered

def initial_counts():
    pass


if __name__ == '__main__':
    sigma = 2

    # Initial counts: count how many times each item occurs
    # Prune those that do not appear at least sigma times 
    counts = {}
    # O(zn) where n is the number of transactions and z is the number of unique counts
    # Memory intensive: have to keep all unique items and their counts in memory
    for line in open('retail_25k.dat'):
        for x in line.split():
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1 
    keys = prune(counts, sigma)

    # Generate all pairs from pruned keys 
    # Memory intensive: have to keep all pairs in memory
    pairs = {}
#    ctr = 1
    for pair in tqdm(itertools.combinations(keys, 2)):
        pairs[pair] = 0
#        ctr += 1
#        if ctr == 10:
#            break
    # Count occurrences in the dataset
    for line in tqdm(open('retail_25k.dat')):
        items = line.split()
        for (x, y) in pairs:
            if x in items and y in items:
                pairs[(x, y)] += 1
    #keys = prune(counts, sigma)
    ipdb.set_trace()
