# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_name(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_quality_change(self):
        items = [Item("Test Item", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(29, items[0].quality)

    def test_max_quality(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_min_quality(self):
        items = [Item("Min item", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_change_after_sell_by(self):
        items = [Item("Test Item", -5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(28, items[0].quality)

    def test_quality_change_on_sell_by(self):
        items = [Item("Test Item", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(28, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)


    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)    

    def test_aged_brie_quality_before_sell_by(self):
        items = [Item("Aged Brie", 5, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(41, items[0].quality)

    def test_aged_brie_quality_after_sell_by(self):
        items = [Item("Aged Brie", -1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(42, items[0].quality)

    def test_backstage_pass_greater_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(31, items[0].quality)

    def test_backstage_pass_under_10_more_than_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(32, items[0].quality)

    def test_backstage_pass_at_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(33, items[0].quality)

    def test_backstage_pass_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured(self):
        items = [Item("Conjured Mana Cake", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(28, items[0].quality)

    def test_conjured_hard(self):
        items = [Item("Conjured Mana Cake", 0, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_conjured_sulfuras(self):
        items = [Item("Conjured Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_conjured_brie(self):
        items = [Item("Conjured Aged Brie", 5, 13)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(15, items[0].quality)

    def test_conjured_brie_after_sell_by(self):
        items = [Item("Conjured Aged Brie", -2, 13)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(17, items[0].quality)

    def test_conjured_backstage_passes_after_sell_by(self):
        items = [Item("Conjured Backstage passes to a TAFKAL80ETC concert", -2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_backstage_passes_after_sell_by(self):
        items = [Item("Conjured Backstage passes to a TAFKAL80ETC concert", 8, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(24, items[0].quality)

    def test_multiple_normal_items(self):
        items = [Item("Milk", 8, 20), Item("Bread", 10, 3), Item("Milk", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)
        self.assertEqual(2, items[1].quality)
        self.assertEqual(9, items[2].quality)

    def test_multiple_wacky_items(self):
        items = [Item("Conjured Milk", 8, 20), Item("Backstage passes to a TAFKAL80ETC concert", 10, 3), Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)
        self.assertEqual(5, items[1].quality)
        self.assertEqual(11, items[2].quality)

        
if __name__ == '__main__':
    unittest.main()
