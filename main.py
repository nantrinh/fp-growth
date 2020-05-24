import ipdb
from collections import defaultdict
import preprocess as pp
import fp_tree


def main(transactions, sigma=2):
    # Preprocess transactions
    # Filter out those items that do not show up at least sigma times overall
    # Sort items per transaction in order of frequency (highest to lowest)
    filtered_transactions, filtered_counts = pp.preprocess(transactions, sigma)

    for t in filtered_transactions:
        print(t)

    for (k, v) in filtered_counts.items():
        print(f'{k}: {v}')

    # Construct FPTree
    tree = fp_tree.FPTree() 
    for t in filtered_transactions:
        tree.add(t)

    # Get prefix paths 
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

    # https://www.geeksforgeeks.org/ml-frequent-pattern-growth-algorithm/
    transactions = [
        'ekmnoy', 'deknoy', 'aekm', 'ckmuy', 'ceikoo'
    ]
    main(transactions, 3)
