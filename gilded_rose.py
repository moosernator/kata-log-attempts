# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.item_quality_increment = 1

    def update_quality(self):
        for item in self.items:

            self.check_special_items(item)

            self.check_sell_by_date(item)

            self.lower_sell_in(item)

            self.item_quality_increment = 1

    def check_special_items(self, item):

            self.check_sulfuras(item)

            self.check_aged_brie(item)

            self.check_backstage_passes(item)

            self.check_conjured(item)

    def check_sulfuras(self, item):
        if "sulfuras" in item.name.lower():
            self.item_quality_increment = 0

    def check_aged_brie(self, item):
        if "brie" in item.name.lower():
            self.item_quality_increment = -1

    def check_backstage_passes(self, item):
        if "backstage" in item.name.lower():
            if 5 < item.sell_in < 11:
                self.item_quality_increment = -2
            elif 0 < item.sell_in < 6:
                self.item_quality_increment = -3
            elif item.sell_in <= 0:
                item.quality = 0
                self.item_quality_increment = 0
            else:
                self.item_quality_increment = -1

    def check_conjured(self, item):
        if "conjured" in item.name.lower():
            self.item_quality_increment *= 2

    def check_sell_by_date(self, item):
        if item.quality >= 0:
            self.check_before_or_after_sell_by(item)
            self.check_max_quality(item)
            self.check_min_quality(item)

    def check_before_or_after_sell_by(self, item):
        if item.sell_in <= 0:
            self.item_quality_increment *= 2
            item.quality -= self.item_quality_increment

        else:
            item.quality -= self.item_quality_increment
    
    def check_max_quality(self, item):
        if item.quality > 50 and item.quality != 80:
            item.quality = 50

    def check_min_quality(self, item):
        if item.quality < 0:
            item.quality = 0

    def lower_sell_in(self, item):
        if "sulfuras" not in item.name.lower():
           item.sell_in -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
