import fp_tree as fpt
import preprocess as pp
import unittest
from collections import defaultdict
import ipdb


class TestFPTree(unittest.TestCase):

    def setUp(self):
        filtered_transactions = [[4, 3, 2], [4, 3, 2, 7], [4, 7], [4, 3]]
        counts = {2: 2, 3: 3, 4: 4, 7: 2}
        self.example = {
            'filtered_transactions': filtered_transactions,
            'counts': counts
        }

    def test_add(self):
        """
        FPTree is created properly
        """
        tree = fpt.FPTree()
        for t in self.example['filtered_transactions']:
            tree.add(t)

        expected_counts = [4, 3, 2, 4, 3, 2, 1, 4, 1, 4, 3]
        k = 0

        for t in self.example['filtered_transactions']:
            # print(f'Processing transaction {t}')
            node = tree.root
            for item in t:
                # print(f'Processing item {item}')
                node = node.child(item)
                self.assertEqual(node.value, item)
                self.assertEqual(node.count, expected_counts[k])
                k += 1
                # print(node.count)

if __name__ == '__main__':
    unittest.main()