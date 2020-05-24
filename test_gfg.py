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
            'count_order': [[5, 4, 2, 1, 1], [5, 4, 2, 1], [5, 4, 2], [5, 1, 1], [5, 4, 2]] 
        }

    def test_add(self):
        """
        FPTree creation
        """
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

#        # Check linked lists (used to generate prefix path subtrees) 
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