import fp_tree as fpt
import preprocess as pp
import unittest
from collections import defaultdict
import ipdb


class TestFPTree(unittest.TestCase):

    def setUp(self):
        self.example = {
            'filtered_transactions': ['kemoy', 'keoy', 'kem', 'kmy', 'keo'],
            'counts': {'k': 5, 'e': 4, 'm': 3, 'o': 3, 'y': 3},
            'traversal_order': 'yomek',
            'count_order': [[5, 4, 2, 1, 1], [5, 4, 2, 1], [5, 4, 2], [5, 1, 1], [5, 4, 2]],
            'll_order': [[1, 1, 1], [1, 2], [2, 1], [4], [5]],
            'prefix_paths': {
                'y': [['kemo', 1], ['keo', 1], ['km', 1]],
                'o': [['kem', 1], ['ke', 2]],
                'm': [['ke', 2], ['k', 1]],
                'e': [['k', 4]],
                'k': []
            },
            'tree': None,
        }
        tree = fpt.FPTree()
        for t in self.example['filtered_transactions']:
            tree.add(t)
        self.example['tree'] = tree

    def test_fptree_creation(self):
        # Check value, count, and parent
        for i, t in enumerate(self.example['filtered_transactions']):
            # print(f'Processing transaction {t}')
            prev = self.example['tree'].root
            for j, item in enumerate(t):
                # print(f'Processing item {item}')
                curr = prev.child(item)
                self.assertEqual(curr.value, item)
                self.assertEqual(curr.count, self.example['count_order'][i][j])
                # print(curr.count)
                self.assertEqual(curr.parent, prev)
                prev = curr

    def test_fptree_linked_lists(self):
        for i, item in enumerate(self.example['traversal_order']):
            # print(f'Evaluating {item}')
            j = 0
            # first one is a dummy
            ll_node = self.example['tree'].linked_lists[item].head
            while ll_node.next:
                ll_node = ll_node.next
                # the value of the ll node points to an FPNode
                # print(f"actual: {ll_node.value.count} expected: {self.example['ll_order'][i][j]}")
                self.assertEqual(
                    ll_node.value.count,
                    self.example['ll_order'][i][j])
                j += 1

    def test_prefix_paths(self):
        for item in self.example['traversal_order']:
            paths = self.example['tree'].prefix_paths(item)
            # print(item)
            paths = [[''.join(list(p[0])), p[1]] for p in paths]
            # print(paths)
            self.assertEqual(
                len(self.example['prefix_paths'][item]), len(paths))
            for p in paths:
                self.assertTrue(p in self.example['prefix_paths'][item])


if __name__ == '__main__':
    unittest.main()
