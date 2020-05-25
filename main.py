import ipdb

import preprocess as pp
import fp_tree
import fp_helper


def main(transactions, min_length, min_support,
         file_location='output.txt'):
    # Preprocess transactions
    # Filter out those items that do not show up at least sigma times overall
    # Sort items per transaction in order of frequency (highest to lowest)
    filtered_transactions, filtered_counts = pp.preprocess(
        transactions, min_support)

    # Construct FPTree
    tree = fp_tree.FPTree()
    for t in filtered_transactions:
        tree.add(t)

    # Generate frequent patterns
    for (pattern, count) in fp_helper.frequent_patterns(tree, min_length, min_support):
        print(pattern, count)

    # Write to file
    #file_obj = open(file_location, 'w')

if __name__ == '__main__':
    # assuming data can fit in memory
    # transactions = [list(map(int, line.split()))
    #                 for line in open('retail_25k.dat')]
    # sigma = 4
    # min_length = 3
    transactions = ['ab', 'bcd', 'acde', 'ade', 'abc', 'abcd', 'a', 'abc', 'abd', 'bce']
    min_length = 3
    min_support = 2

    import time
    start = time.perf_counter()
    main(transactions, min_length, min_support)
    end = time.perf_counter()
    print(f"Finished in {end - start:0.4f} seconds")
