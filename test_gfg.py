import unittest
from collections import defaultdict

import fp_tree as fpt
import fp_helper
from examples import examples

import ipdb

class TestFPTree(unittest.TestCase):

    def setUp(self):
        self.examples = examples()

    def test_fptree_creation(self):
        for example in self.examples:
            # Check value, count, and parent
            for i, t in enumerate(example['filtered_transactions']):
                # print(f'Processing transaction {t}')
                prev = example['tree'].root
                for j, item in enumerate(t):
                    # print(f'Processing item {item}')
                    curr = prev.child(item)
                    self.assertEqual(curr.value, item)
                    self.assertEqual(curr.count, example['count_order'][i][j])
                    # print(curr.count)
                    self.assertEqual(curr.parent, prev)
                    prev = curr

    def test_fptree_linked_lists(self):
        for example in self.examples:
            for i, item in enumerate(example['traversal_order']):
                # print(f'Evaluating {item}')
                j = 0
                # first one is a dummy
                ll_node = example['tree'].linked_lists[item].head
                while ll_node.next:
                    ll_node = ll_node.next
                    # the value of the ll node points to an FPNode
                    # print(f"actual: {ll_node.value.count} expected:
                    # {self.example['ll_order'][i][j]}")
                    self.assertEqual(
                        ll_node.value.count,
                        example['ll_order'][i][j])
                    j += 1

    def test_prefix_paths(self):
        """Also known as conditional pattern base"""
        for example in self.examples:
            for item in example['traversal_order']:
                paths = example['tree'].prefix_paths(item)
                # print(item)
                # forcing a list and joining to compare with the expected output
                # I defined in the example
                paths = [[list(p[0]), p[1]] if p[0] else p for p in paths]
                # print(paths)
                self.assertEqual(
                    len(example['prefix_paths'][item]), len(paths))
                for p in paths:
                    self.assertTrue(p in example['prefix_paths'][item])

    def test_conditional_fptree_elements(self):
        """Longest common prefixes for each prefix path"""
        for example in self.examples:
            for item in example['traversal_order']:
                paths = example['prefix_paths'][item]
                output = fp_helper.conditional_fptree_elements(paths)
                # print(f"output: {output} expected: {example['lcp'][item]}")
                self.assertEqual(output, example['lcp'][item])

    def test_frequent_patterns(self):
        for example in self.examples:
            for item in example['traversal_order']:
                lcp = example['lcp'][item]
                patterns = fp_helper.frequent_patterns(item, lcp)
                patterns = [[set(p[0]), p[1]] for p in patterns]
                # print(patterns)
                # print(f"{item}: output: {patterns} expected: {example['frequent_patterns'][item]}")
                self.assertEqual(
                    len(patterns), len(
                        example['frequent_patterns'][item]))
                for p in patterns:
                    self.assertTrue(p in example['frequent_patterns'][item])

    def test_write_to_file(self):
        for example in self.examples:
            file_obj = open('temp.txt', 'w')
            for item in example['traversal_order']:
                lcp = example['lcp'][item]
                patterns = fp_helper.frequent_patterns(item, lcp)
                fp_helper.write(file_obj, patterns)
            file_obj.close()


if __name__ == '__main__':
    unittest.main()
