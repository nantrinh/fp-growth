import sys
import unittest
from collections import defaultdict

from fp_growth import FPGrowth 
from main import custom_format

class TestFPGrowth(unittest.TestCase):
    def valid_solution_line(self, pattern_size, support, items, min_length, min_support):
        """
        line is an iterable in the format:
        pattern_size, support/count, item1, item2, ... 

        Does the following checks:
        pattern_size == len(items)
        pattern_size >= min_length
        support >= min_support
        """
        self.assertEqual(pattern_size, len(items))
        self.assertTrue(pattern_size >= min_length)
        self.assertTrue(support >= min_support)

    def valid_solution(self, filename, min_length, min_support, nums=False):
        """
        Reads in a file and checks
        - if each line is a valid solution
        - that there are no duplicate patterns
        """
        unique_items = set()
        with open(filename) as f: 
            for line in f:
                pattern_size, support, *items = line.strip().split(', ')
                pattern_size = int(pattern_size)
                support = int(support)
                if nums:
                    items = map(int, items)
                items.sort
                items = tuple(items)

                self.assertTrue(items not in unique_items)
                unique_items.add(items)

                self.valid_solution_line(pattern_size, support, items, min_length, min_support)

    def test_retail(self):
        # transactions = [list(map(int, line.split()))
        #                 for line in open('retail_25k.dat')]
        transactions = [list(map(int, line.split()))
                        for line in open('retail_100.dat')]

        test_cases = ((1, 2), (2, 2), (2, 3), (3, 2), (3, 3), (3, 4), (4, 3), (4, 4))
        for min_length, min_support in test_cases: 
            print(f"CHECKING RETAIL {min_length} {min_support}")
            output_filename = 'output.txt'
            sys.stdout = open(output_filename, 'w')
            
            fpg = FPGrowth(min_length=min_length, min_support=min_support)
            for itemset, support in fpg.frequent_itemsets(transactions):
                print(custom_format(itemset, support))

            sys.stdout.close()
            sys.stdout = sys.__stdout__

            self.valid_solution(output_filename, min_length=min_length, min_support=min_support)
            self.same_solution(
                f'solutions/retail_solution_{min_length}_{min_support}.txt',
                output_filename)

    def test_gfg_examples(self):
        raw = ['ekmnoy', 'deknoy', 'aekm', 'ckmuy', 'ceiko']
        transactions = [list(x) for x in raw]
        test_cases = ((1, 2), (2, 2), (2, 3), (3, 2), (3, 3), (3, 4), (4, 3))
        for min_length, min_support in test_cases: 
            print(f"CHECKING GFG {min_length} {min_support}")
            output_filename = 'output.txt'
            sys.stdout = open(output_filename, 'w')
            
            fpg = FPGrowth(min_length=min_length, min_support=min_support)
            for itemset, support in fpg.frequent_itemsets(transactions):
                print(custom_format(itemset, support))

            sys.stdout.close()
            sys.stdout = sys.__stdout__
            self.same_solution(
                f'solutions/gfg_solution_{min_length}_{min_support}.txt',
                output_filename)

    def test_slides_examples(self):
        raw = ['ab', 'bcd', 'acde', 'ade', 'abc', 'abcd', 'a', 'abc', 'abd', 'bce']
        transactions = [list(x) for x in raw]

        test_cases = ((1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (4, 3))
        for min_length, min_support in test_cases: 
            print(f"CHECKING SLIDES {min_length} {min_support}")
            output_filename = 'output.txt'
            sys.stdout = open(output_filename, 'w')
            
            fpg = FPGrowth(min_length=min_length, min_support=min_support)
            for itemset, support in fpg.frequent_itemsets(transactions):
                print(custom_format(itemset, support))

            sys.stdout.close()
            sys.stdout = sys.__stdout__
            self.same_solution(
                f'solutions/slides_solution_{min_length}_{min_support}.txt',
                output_filename)


    def same_solution(self, solution, my_answer):
        s_list = [] 
        my_list = [] 

        with open(solution) as f:
            for line in f:
                pattern_size, support, *items = line.strip().split(', ')
                s_list.append((pattern_size, support, set(items)))

        with open(my_answer) as f:
            for line in f:
                pattern_size, support, *items = line.strip().split(', ')
                my_list.append((pattern_size, support, set(items)))

        # self.assertEqual(len(my_list), len(s_list), f'my len: {len(my_list)} solution len: {len(s_list)}')
        if len(my_list) != len(s_list):
            print(len(my_list), len(s_list))
        for a in my_list:
            if a not in s_list:
                print(f'{a} in my answer but not in solution')

        for b in s_list:
           if b not in my_list:
               print(f'{b} in solution but not in my answer')
           
            # self.assertTrue(a in s_list, msg=f"{a} not found")

if __name__ == '__main__':
    unittest.main()
