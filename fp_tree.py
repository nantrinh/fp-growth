import ipdb
from collections import defaultdict
from typing import List


def main(transactions, sigma=2):
    preconstruction(transactions, sigma)


def preconstruction(transactions, sigma):
    # Count how many times each item occurs across all transactions
    counts = initial_count(transactions)
    # Only keep the items that occur at least sigma times in the transactions
    counts = prune(counts, sigma)
    # Filter out the items per transaction
    # Sort the items in each transaction in order of how often
    # they occur across all transactions
    transactions = clean(transactions, counts)

    ipdb.set_trace()


def initial_count(transactions):
    """
    Return a dictionary containing total counts of each item
    across all transactions
    """
    counts = defaultdict(lambda: 0)
    for t in transactions:
        for item in t:
            counts[item] += 1
    return counts


def prune(counts, sigma):
    return dict((k, v) for (k, v) in counts.items() if v >= sigma)


def clean(transactions, counts_with_min_support):
    transactions = [list(set(t).intersection(
        set(counts_with_min_support.keys()))) for t in transactions]
    for t in transactions:
        t.sort(key=lambda v: counts_with_min_support[v], reverse=True)
    return transactions


if __name__ == '__main__':
    # assuming data can fit in memory
    transactions = [list(map(int, line.split()))
                    for line in open('retail_25k.dat')]
    main(transactions, 2)
