import ipdb

import preprocess as pp
import fp_tree
import fp_helper


def main(transactions, min_support=1, min_length=1,
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

    # Get prefix paths, taking min_length into consideration
    # Get conditional fptree elements (longest common prefix)
    # Generate frequent patterns
    # Write to file
    file_obj = open(file_location, 'w')
    for item in filtered_counts:
        print(f"Processing item {item}")
        # passing min_length - 1 as the min_length_of_prefix because the
        # total length of a pattern will be prefix + item, or prefix + 1
        prefix_paths = tree.prefix_paths(item, min_length - 1)
        conditional_fptree_elements = fp_helper.conditional_fptree_elements(
            prefix_paths, min_support)
        print(f'{item}: {conditional_fptree_elements}')
        # passing min_length - 1 as the min_length_of_prefix because the
        # total length of a pattern will be prefix + item, or prefix + 1
        frequent_patterns = fp_helper.frequent_patterns(
            item, conditional_fptree_elements, min_length - 1)
        fp_helper.write(file_obj, frequent_patterns)
    file_obj.close()

if __name__ == '__main__':
    # assuming data can fit in memory
    transactions = [list(map(int, line.split()))
                    for line in open('retail_25k.dat')]
    sigma = 4
    min_length = 3

    import time
    start = time.perf_counter()
    main(transactions, sigma, min_length, 'retail_output.txt')
    end = time.perf_counter()
    print(f"Finished in {end - start:0.4f} seconds")
