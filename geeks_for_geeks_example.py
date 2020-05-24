import ipdb
from collections import defaultdict
import preprocess as pp
import fp_tree


def main(transactions, sigma=2):
    # Preprocess transactions
    # Filter out those items that do not show up at least sigma times overall
    # Sort items per transaction in order of frequency (highest to lowest)
    filtered_transactions, filtered_counts = pp.preprocess(transactions, sigma)

    """
    Expected:
    ['k', 'e', 'o', 'm', 'y']
    ['k', 'e', 'y', 'o']
    ['k', 'e', 'm']
    ['k', 'y', 'm']
    ['k', 'e', 'o']
    """
    for t in filtered_transactions:
        print(t)

    """
    Expected:
    o: 3
    m: 3
    y: 3
    e: 4
    k: 5
    """
    for (k, v) in filtered_counts.items():
        print(f'{k}: {v}')

    # Construct FPTree
    tree = fp_tree.FPTree() 
    for t in filtered_transactions:
        tree.add(t)

    """
    Expected:
    k: [[]]
    e: [['k']]
    o: [['e', 'k'], ['y', 'e', 'k']]
    m: [['o', 'e', 'k'], ['e', 'k'], ['y', 'k']]
    y: [['m', 'o', 'e', 'k'], ['e', 'k'], ['k']]
    """
    # Get all prefix paths (no pruning) 
    prefix_paths = tree.all_prefix_paths() 
    for (k, v) in prefix_paths.items():
        print(f'{k}: {v}')

    # 
    ipdb.set_trace()


if __name__ == '__main__':
    # assuming data can fit in memory
#    transactions = [list(map(int, line.split()))
#                    for line in open('retail_25k.dat')]
#    transactions = [
#        [1, 2, 3, 4, 5, 6],
#        [2, 3, 4, 7, 8, 9],
#        [4, 7],
#        [3, 4]
#    ]

# Resources: https://wimleers.com/sites/wimleers.com/files/FP-Growth%20presentation%20handouts%20%E2%80%94%C2%A0Florian%20Verhein.pdf
    # https://www.geeksforgeeks.org/ml-frequent-pattern-growth-algorithm/
    transactions = [
        'ekmnoy', 'deknoy', 'aekm', 'ckmuy', 'ceikoo'
    ]
    main(transactions, 3)
