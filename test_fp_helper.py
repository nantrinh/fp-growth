import unittest

import fp_helper
from examples import examples


class TestFPHelper(unittest.TestCase):

    def setUp(self):
        self.examples = examples()

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
