import unittest

from Dominator.solution import findADominatorIndex

class TestBinaryGap(unittest.TestCase):

    def test_findTheLongestBinaryGap(self):
        self.assertEqual(findADominatorIndex([3, 2, 3, 4, 3, 3, 3, -1]), 0)
        self.assertEqual(findADominatorIndex([3]), 0)

if __name__ == '__main__':
    unittest.main()