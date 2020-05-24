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
            'count_order': [[5, 4, 2, 1, 1], [5, 4, 2, 1], [5, 4, 2], [5, 1, 1], [5, 4, 2]],
            'll_order': [[1, 1, 1], [1, 2], [2, 1], [4], [5]] 
        }

    def test_fptree_creation(self):
        tree = fpt.FPTree()
        for t in self.example['filtered_transactions']:
            tree.add(t)

        # Check value, count, and parent 
        for i, t in enumerate(self.example['filtered_transactions']):
            # print(f'Processing transaction {t}')
            prev = tree.root
            for j, item in enumerate(t):
                # print(f'Processing item {item}')
                curr = prev.child(item)
                self.assertEqual(curr.value, item)
                self.assertEqual(curr.count, self.example['count_order'][i][j])
                # print(curr.count)
                self.assertEqual(curr.parent, prev)
                prev = curr

    def test_fptree_linked_lists(self):
        tree = fpt.FPTree()
        for t in self.example['filtered_transactions']:
            tree.add(t)
        
        for i, item in enumerate('yomek'):
            print(f'Evaluating {item}')
            j = 0
            # first one is a dummy
            ll_node = tree.linked_lists[item].head
            while ll_node.next:
                ll_node = ll_node.next
                # the value of the ll node points to an FPNode
                # print(f"actual: {ll_node.value.count} expected: {self.example['ll_order'][i][j]}")
                self.assertEqual(ll_node.value.count, self.example['ll_order'][i][j])
                j += 1



#        expected_ll_counts = {
#            4: [4],
#            3: [3],
#            2: [2],
#            7: [1, 1]
#        } 
#
#        for (k, exp) in expected_ll_counts.items():
#            # print(f'Checking item {k}')
#            node = tree.linked_lists[k].head
#            self.assertEqual(node.value, None)
#            i = 0
#            while node.next:
#                # print(f'Count: {node.next.value.count}')
#                self.assertEqual(node.next.value.count, exp[i])
#                i += 1
#                node = node.next

    #def test_prefix_paths(self):
    #    # TODO: should probably manually create a tree here instead
    #    tree = fpt.FPTree()
    #    for t in self.example['filtered_transactions']:
    #        tree.add(t)
    #    
    #    answer = {
    #        7: [[2, 3, 4], [4]],
    #        2: [[3, 4]],
    #        3: [[4]],
    #        4: [[]]
    #    }

    #    for k in answer:
    #        # print(f'Processing item {k}')
    #        output = tree.prefix_paths(k)
    #        # print(f'Got {output}, expected {answer[k]}')
    #        self.assertEqual(output, answer[k])


if __name__ == '__main__':
    unittest.main()