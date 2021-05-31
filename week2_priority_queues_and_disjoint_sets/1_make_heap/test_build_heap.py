import unittest
import build_heap as m

class TestUtils(unittest.TestCase):
    def test_parent(self):
        self.assertEqual(0, m.parent(1))
        self.assertEqual(2, m.parent(5))
        self.assertEqual(2, m.parent(6))


    def test_left_right(self):
        self.assertEqual(1, m.left(0))
        self.assertEqual(2, m.right(0))
        self.assertEqual(5, m.left(2))
        self.assertEqual(6, m.right(2))

    def test_family(self):
        self.assertEqual(15, m.left(m.parent(15)))
        self.assertEqual(16, m.right(m.parent(16)))
        self.assertEqual(29, m.left(m.parent(29)))
        self.assertEqual(30, m.right(m.parent(30)))

    def test_len_2(self):
        swaps = m.build_heap([0, 0])
        self.assertEqual([], swaps)

if __name__ == '__main__':
    unittest.main()
