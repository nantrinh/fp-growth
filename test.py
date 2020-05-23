import fp_tree
import unittest
from collections import defaultdict
import ipdb


class TestStringMethods(unittest.TestCase):

    def test_initial_count(self):
        transactions = [
            [1, 2, 3, 4, 5, 6],
            [2, 3, 4, 7, 8, 9],
            [4, 7],
            [2],
            [3, 4]
        ]
        answer = defaultdict(lambda: 0)
        for t in transactions:
            for item in t:
                answer[item] += 1
        print(answer)
        self.assertEqual(fp_tree.initial_count(transactions), answer)

    def test_prune(self):
        counts = {1: 1, 2: 3, 3: 3, 4: 4, 5: 1, 6: 1, 7: 2, 8: 1, 9: 1}
        sigma = 2
        answer = {2: 3, 3: 3, 4: 4, 7: 2}
        self.assertEqual(fp_tree.prune(counts, sigma), answer)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
