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
    with open('retail_25k.dat') as f:
        transactions = [list(map(int, line.split()))
                    for line in f]

    test_cases = [(3, 4)]

    for min_length, min_support in test_cases: 
        output_filename = f'outputs/{prefix}_{min_length}_{min_support}_output.txt'
        f = open(output_filename, 'w')
        for res in run_fp(transactions, min_length=min_length, min_support=min_support):
            f.write(res + '\n')
        f.close()