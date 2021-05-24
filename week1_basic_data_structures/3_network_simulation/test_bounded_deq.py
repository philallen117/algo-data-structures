import unittest
from process_packages import BoundedDeque


class Test(unittest.TestCase):
    def test_empty(self):
        q = BoundedDeque(1)
        self.assertTrue(q.empty())
        with self.assertRaises(IndexError):
            q.take()

    def test_peek(self):
        q = BoundedDeque(2)
        q.add(1)
        self.assertEqual(q.peek_last(), 1)
        q.add(2)
        self.assertEqual(q.peek_last(), 2)
        q.take()
        self.assertEqual(q.peek_last(), 2)
        q.take()
        with self.assertRaises(IndexError):
            q.peek_last()

    def test_full(self):
        q0 = BoundedDeque(0)
        self.assertTrue(q0.full())
        with self.assertRaises(IndexError):
            q0.add(1)
        q = BoundedDeque(1)
        q.add(1)
        self.assertTrue(q.full())
        with self.assertRaises(IndexError):
            q.add(2)

    def test_add_take(self):
        q = BoundedDeque(4)
        q.add(1)
        q.add(2)
        self.assertEqual(q.take(), 1)
        q.add(3)
        q.add(4)
        self.assertFalse(q.full())
        self.assertEqual(q.take(), 2)
        self.assertEqual(q.take(), 3)
        self.assertEqual(q.take(), 4)
        self.assertTrue(q.empty())

    def test_drop_until(self):
        q = BoundedDeque(5)
        for i in range(5): q.add(i)
        q.drop_until(lambda i: i >= 2)
        self.assertEqual(q.take(), 2)
        q.drop_until(lambda i: i >= 5)
        self.assertTrue(q.empty())

if __name__ == '__main__':
    unittest.main()
