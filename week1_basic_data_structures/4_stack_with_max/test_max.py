import unittest
from stack_with_max import StackWithMax

class TestMax(unittest.TestCase):
    def test_it(self):
        s = StackWithMax()
        s.push(1)
        self.assertTrue(not s.empty())
        s.push(5)
        self.assertTrue(5 == s.max())
        s.push(3)
        self.assertTrue(5 == s.max())
        s.push(6)
        self.assertTrue(6 == s.max())
        s.pop()
        self.assertTrue(5 == s.max())
        s.pop()
        s.pop()
        self.assertTrue(1 == s.max())


if __name__ == '__main__':
    unittest.main()
