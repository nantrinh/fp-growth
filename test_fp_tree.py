import fp_tree as fpt
import preprocess as pp
import unittest
from collections import defaultdict
import ipdb


class TestFPTree(unittest.TestCase):

    def setUp(self):
        filtered_transactions = [[4, 3, 2], [4, 3, 2, 7], [4, 7], [4, 3]]
        self.example = {
            'filtered_transactions': filtered_transactions,
        }

    def test_add(self):
        tree = fpt.FPTree()
        for t in self.example['filtered_transactions']:
            tree.add(t)

        for t in self.example['filtered_transactions']:
            node = tree.root
            for item in t:
                self.assertEqual(node.child(item).value, item)
                node = node.child(item)

if __name__ == '__main__':
    unittest.main()