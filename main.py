from fp_growth import FPGrowth 

def custom_format(itemset, support):
    """pattern_size, support/count, item1, item2, ..."""
    return f"{len(itemset)}, {support}, {', '.join(map(str, itemset))}"

if __name__ == "__main__":
    # transactions = [list(map(int, line.split()))
    #                 for line in open('retail_25k.dat')]
    # min_length = 3
    # min_support = 4

    # slides example
    raw = ['ab', 'bcd', 'acde', 'ade', 'abc', 'abcd', 'a', 'abc', 'abd', 'bce']
    transactions = [list(x) for x in raw]
    min_length = 1
    min_support = 2

    fpg = FPGrowth(min_length=min_length, min_support=min_support)

    for itemset, support in fpg.frequent_itemsets(transactions):
        print(custom_format(itemset, support))