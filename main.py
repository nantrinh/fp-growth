from fp_growth import FPGrowth 

def custom_format(itemset, support):
    """pattern_size, support/count, item1, item2, ..."""
    return f"{len(itemset)}, {support}, {', '.join(map(str, itemset))}"

def run_fp(transactions, min_length, min_support):
    fpg = FPGrowth(min_length=min_length, min_support=min_support)
    for itemset, support in fpg.frequent_itemsets(transactions):
        yield custom_format(itemset, support)

if __name__ == "__main__":

    prefix = 'retail_25k'
    transactions = [list(map(int, line.split())) for line in open('retail_25k.dat')]

    min_length = 3
    min_support = 4

    output_filename = 'output.txt'
    f = open(output_filename, 'w')
    for res in run_fp(transactions, min_length=min_length, min_support=min_support):
        f.write(res + '\n')
    f.close()