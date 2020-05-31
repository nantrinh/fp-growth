"""
Functions to preprocess transaction data
"""

from collections import defaultdict

def preprocess(transactions, sigma):
    # Count how many times each item occurs across all transactions
    # Only keep the items that occur at least sigma times in the transactions
    filtered_counts = prune(initial_count(transactions), sigma)
    # Filter out the items per transaction
    # Sort the items in each transaction in order of how often
    # they occur across all transactions
    filtered_transactions = clean(transactions, filtered_counts)
    return filtered_transactions, filtered_counts

def initial_count(transactions):
    """
    Return a dictionary containing total counts of each item
    across all transactions
    """
    counts = defaultdict(lambda: 0)
    for t in transactions:
        for item in set(t):
            counts[item] += 1
    return counts


def prune(counts, sigma):
    return dict((k, v) for (k, v) in counts.items() if v >= sigma)


def clean(transactions, counts_with_min_support):
    transactions = [list(set(t).intersection(
        set(counts_with_min_support.keys()))) for t in transactions]
    for t in transactions:
        # if there's a tie in value, put the larger key first
        t.sort(key=lambda k: (counts_with_min_support[k], k), reverse=True)
    return transactions

