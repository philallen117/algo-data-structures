import unittest
import tree_height as m


class TestTreeHeight(unittest.TestCase):

    def test_s0(self):
        parents = [ -1 ]
        self.assertEqual(0, m.compute_height(1, parents))

    def test_s1(self):
        parents = [ 4, -1, 4, 1, 1 ]
        self.assertEqual(3, m.compute_height(5, parents))

    def test_s2(self):
        parents = [ -1, 0, 4, 0, 3 ]
        self.assertEqual(4, m.compute_height(5, parents))


if __name__ == '__main__':
    unittest.main()
