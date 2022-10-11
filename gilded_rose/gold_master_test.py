import gilded_rose as gr

def test_gold_master(capfd):
    items = [
             gr.Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             gr.Item(name="Aged Brie", sell_in=2, quality=0),
             gr.Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             gr.Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             gr.Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             gr.Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             gr.Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             gr.Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             gr.Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]
    days = 20

    compare = open("gold_master_compare.txt").read()

    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        gr.GildedRose(items).update_quality()
    
    out, err = capfd.readouterr()

    assert out == compare
