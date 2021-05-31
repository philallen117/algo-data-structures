import unittest
from hypothesis import given, strategies as st
from math import log, ceil

import build_heap as m

class HypTests(unittest.TestCase):

    @given(data=st.lists(st.integers(), min_size=1, max_size=63))
    def test_props(self, data):
        data_sorted = sorted(data)
        m.build_heap(data)
        data_heaped_sorted = sorted(data)
        self.assertEqual(data_heaped_sorted, data_sorted, "preserves elements")
        for i in range(1, len(data)):
            j = len(data) - i
            self.assertTrue(data[j] >= data[m.parent(j)], "heap property - {}".format(j))
        
    @given(data=st.lists(st.integers(), min_size=4, max_size=128))
    def test_perf(self, data):
        swaps = m.build_heap(data)
        self.assertLessEqual(len(swaps), 4 * len(data))
        
if __name__ == '__main__':
    unittest.main()
