import unittest

from BinaryGap.solution import findTheLongestBinaryGap

class TestBinaryGap(unittest.TestCase):

    def test_findTheLongestBinaryGap(self):
        self.assertEqual(findTheLongestBinaryGap(4), 0)

if __name__ == '__main__':
    unittest.main()