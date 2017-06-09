"""Test cases for class to audit differences in groups of items sorted into tiers by having particular values."""

import unittest
import TieredLists

class TestTieredLists(unittest.TestCase):

    def test_init(self):
        tiers = [2, 4, 8, 16]
        tl = TieredLists(tiers)
        for t in tiers:
            self.assertIn(t, tl.tiers)
            self.assertIn(t, tl.bags)

    def test_get_tier(self):
        tiers = [2, 4, 8, 16]
        tl = TieredLists(tiers)
        self.assertIsNone(tl.get_tier(0))
        self.assertEqual(2, tl.get_tier(2))
        self.assertEqual(2, tl.get_tier(3))
        self.assertEqual(4, tl.get_tier(5))
        self.assertEqual(16, tl.get_tier(200))

    def test_bag(self):
        tiers = [2, 4, 8, 16]
        tl = TieredLists(tiers)
        for t in tiers:
            self.assertIsNotNone(tl.bag(t))

    def test_add(self):
        tiers = [2, 4, 8, 16]
        tl = TieredLists(tiers)
        path_1 = '/a/short/url'
        path_2 = '/the/quick/brown/fox/is/dead'
        path_3 = '/news/bangor/2017/06/05/reality-winner/'
        tl.add(2, path_1)
        tl.add(20, path_2)
        self.assertIn(path_1, tl.bag(2))
        self.assertIn(path_2, tl.bag(16))
        result = tl.add(1, path_3)
        self.assertIsNone(result)



if __name__ == '__main__':
    unittest.main()