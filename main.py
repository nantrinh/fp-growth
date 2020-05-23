import ipdb
from collections import defaultdict
import preprocess as pp
import fp_tree


def main(transactions, sigma=2):
    filtered_transactions, filtered_counts = pp.preprocess(transactions, sigma)
    header = fp_tree.header_dict(filtered_counts)
    ipdb.set_trace()


if __name__ == '__main__':
    # assuming data can fit in memory
    transactions = [list(map(int, line.split()))
                    for line in open('retail_25k.dat')]
    main(transactions, 2)
