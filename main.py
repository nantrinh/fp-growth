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

    # Write to file
    file_obj = open(file_location, 'w')

    # Generate frequent patterns
    for (pattern, support) in fp_helper.frequent_patterns(tree, min_length, min_support):
        # print(pattern, support)
        fp_helper.write(file_obj, pattern, support)

    file_obj.close()


if __name__ == '__main__':
    transactions = [list(map(int, line.split()))
                    for line in open('retail_25k.dat')]
    min_support = 4
    min_length = 3

    main(transactions, min_length, min_support)