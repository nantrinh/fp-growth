import preprocess as pp
import unittest
from collections import defaultdict


class TestPreprocess(unittest.TestCase):

    def setUp(self):
        transactions = [
            [1, 2, 3, 4, 5, 6],
            [2, 3, 4, 7, 8, 9],
            [4, 7],
            [3, 4]
        ]
        all_counts = {1: 1, 2: 2, 3: 3, 4: 4, 5: 1, 6: 1, 7: 2, 8: 1, 9: 1}
        self.example = {
            'transactions': transactions,
            'all_counts': all_counts
        }

    def test_initial_count(self):
        answer = defaultdict(lambda: 0)
        for t in self.example['transactions']:
            for item in t:
                answer[item] += 1
        self.assertEqual(
            pp.initial_count(
                self.example['transactions']),
            answer)

    def test_prune(self):
        sigma = 2
        answer = {2: 2, 3: 3, 4: 4, 7: 2}
        self.assertEqual(
            pp.prune(
                self.example['all_counts'],
                sigma),
            answer)

    def test_clean(self):
        counts_with_min_support = {2: 2, 3: 3, 4: 4, 7: 2}
        answer = [
            [4, 3, 2],
            [4, 3, 2, 7],
            [4, 7],
            [4, 3]
        ]
        self.assertEqual(
            pp.clean(
                self.example['transactions'],
                counts_with_min_support),
            answer)


if __name__ == '__main__':
    unittest.main()
