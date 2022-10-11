import gilded_rose as gr

def test_name():
    items = [gr.Item("foo", 0, 0)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name


def test_quality_change():
    items = [gr.Item("Test Item", 5, 30)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 29 == items[0].quality

def test_max_quality():
    items = [gr.Item("Aged Brie", 10, 50)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 50 == items[0].quality

def test_min_quality():
    items = [gr.Item("Min item", 10, 0)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 0 == items[0].quality

def test_quality_change_after_sell_by():
    items = [gr.Item("Test Item", -5, 30)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 28 == items[0].quality

def test_quality_change_on_sell_by():
    items = [gr.Item("Test Item", 0, 30)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 28 == items[0].quality
    assert -1 == items[0].sell_in

def test_sulfuras_quality():
    items = [gr.Item("Sulfuras, Hand of Ragnaros", 0, 80)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 80 == items[0].quality    

def test_aged_brie_quality_before_sell_by():
    items = [gr.Item("Aged Brie", 5, 40)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 41 == items[0].quality

def test_aged_brie_quality_after_sell_by():
    items = [gr.Item("Aged Brie", -1, 40)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 42 == items[0].quality

def test_backstage_pass_greater_than_10_days():
    items = [gr.Item("Backstage passes to a TAFKAL80ETC concert", 11, 30)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 31 == items[0].quality

def test_backstage_pass_under_10_more_than_5():
    items = [gr.Item("Backstage passes to a TAFKAL80ETC concert", 8, 30)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 32 == items[0].quality

def test_backstage_pass_at_5():
    items = [gr.Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 33 == items[0].quality

def test_backstage_pass_after_concert():
    items = [gr.Item("Backstage passes to a TAFKAL80ETC concert", -1, 30)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 0 == items[0].quality

def test_conjured():
    items = [gr.Item("Conjured Mana Cake", 5, 30)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 28 == items[0].quality

def test_conjured_hard():
        items = [gr.Item("Conjured Mana Cake", 0, 3)]
        gilded_rose = gr.GildedRose(items)
        gilded_rose.update_quality()
        assert 0 == items[0].quality

def test_conjured_sulfuras():
    items = [gr.Item("Conjured Sulfuras, Hand of Ragnaros", 5, 80)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 80 == items[0].quality

def test_conjured_brie():
    items = [gr.Item("Conjured Aged Brie", 5, 13)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 15 == items[0].quality

def test_conjured_brie_after_sell_by():
    items = [gr.Item("Conjured Aged Brie", -2, 13)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 17 == items[0].quality

def test_conjured_backstage_passes_after_sell_by():
    items = [gr.Item("Conjured Backstage passes to a TAFKAL80ETC concert", -2, 0)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 0 == items[0].quality

def test_conjured_backstage_passes_after_sell_by():
    items = [gr.Item("Conjured Backstage passes to a TAFKAL80ETC concert", 8, 20)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 24 == items[0].quality

def test_multiple_normal_items():
    items = [gr.Item("Milk", 8, 20), gr.Item("Bread", 10, 3), gr.Item("Milk", 5, 10)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 19 == items[0].quality
    assert 2 == items[1].quality
    assert 9 == items[2].quality

def test_multiple_wacky_items():
    items = [gr.Item("Conjured Milk", 8, 20), gr.Item("Backstage passes to a TAFKAL80ETC concert", 10, 3), gr.Item("Aged Brie", 5, 10)]
    gilded_rose = gr.GildedRose(items)
    gilded_rose.update_quality()
    assert 18 == items[0].quality
    assert 5 == items[1].quality
    assert 11 == items[2].quality