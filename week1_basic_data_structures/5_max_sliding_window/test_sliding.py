import unittest
import max_sliding_window as m


class TestSliding(unittest.TestCase):

    def test_mis_1(self):
        s = m.MaxIntStack()
        self.assertTrue(s.empty())
        s.push(1)
        self.assertFalse(s.empty())
        s.push(5)
        self.assertEqual(5, s.max())
        s.push(3)
        self.assertEqual(5, s.max())
        s.push(6)
        self.assertEqual(6, s.max())
        s.pop()
        self.assertEqual(5, s.max())
        s.pop()
        s.pop()
        self.assertEqual(1, s.max())

    def test_mis_reverse(self):
        s = m.MaxIntStack()
        s.push(7)
        s.push(2)
        s.push(5)
        s.push(4)
        s.push(1)
        s.reverse()
        self.assertEqual(7, s.max())
        s.pop()
        self.assertEqual(5, s.max())
        s.pop()
        self.assertEqual(5, s.max())
        s.pop()
        self.assertEqual(4, s.max())
        s.pop()
        self.assertEqual(1, s.max())

    def test_miq_1(self):
        q = m.MaxIntQueue()
        q.add(1)
        q.add(5)
        self.assertEqual(5, q.max())
        q.add(3)
        self.assertEqual(5, q.max())
        q.add(6)
        self.assertEqual(6, q.max())
        q.add(4)
        self.assertEqual(6, q.max())
        # 1 5 3 6 4
        q.add(1)
        self.assertEqual(6, q.max())
        q.take()
        q.add(1)
        self.assertEqual(6, q.max())
        q.take()
        q.add(1)
        self.assertEqual(6, q.max())
        q.take()
        q.add(2)
        self.assertEqual(6, q.max())
        q.take()
        q.add(1)
        self.assertEqual(4, q.max())
        q.take()
        q.add(5)
        self.assertEqual(5, q.max())
        q.take()
#           -----------
# 1 5 3 6 4 1 1 1 2 1 5
#           6 6 6 6 4 5

    def test_msw_1(self):
        seq = [1, 5, 3, 6, 4, 1, 1, 1, 2, 1, 5]
        act1 = m.max_sliding_window(seq, 1)
        self.assertListEqual([1, 5, 3, 6, 4, 1, 1, 1, 2, 1, 5], act1)
        act2 = m.max_sliding_window(seq, 2)
        self.assertListEqual([5, 5, 6, 6, 4, 1, 1, 2, 2, 5], act2)
        act6 = m.max_sliding_window(seq, 6)
        self.assertListEqual([6, 6, 6, 6, 4, 5], act6)


if __name__ == '__main__':
    unittest.main()
