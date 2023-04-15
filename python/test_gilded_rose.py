from gilded_rose import GildedRose, ItemFactory


class TestNormalItem:
    def test_name(self):
        items = [ItemFactory.create("foo", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "foo" == items[0].name

    def test_sellin(self):
        items = [ItemFactory.create("foo", 1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].sell_in

    def test_sellin_negative(self):
        items = [ItemFactory.create("foo", -1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert -2 == items[0].sell_in

    def test_quality_before_sell_date(self):
        items = [ItemFactory.create("foo", 1, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 1 == items[0].quality

    def test_quality_on_sell_date(self):
        items = [ItemFactory.create("foo", 0, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_after_sell_date(self):
        items = [ItemFactory.create("foo", -1, 4)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 2 == items[0].quality

    def test_quality_not_below_zero(self):
        items = [ItemFactory.create("foo", -2, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_not_below_zero2(self):
        items = [ItemFactory.create("foo", 2, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality


class TestSulfuras:
    def test_name(self):
        items = [ItemFactory.create("Sulfuras, Hand of Ragnaros", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "Sulfuras, Hand of Ragnaros" == items[0].name

    def test_sellin(self):
        items = [ItemFactory.create("Sulfuras, Hand of Ragnaros", 1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 1 == items[0].sell_in

    def test_sellin_negative(self):
        items = [ItemFactory.create("Sulfuras, Hand of Ragnaros", -4, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert -4 == items[0].sell_in

    def test_quality_doesnt_change(self):
        items = [ItemFactory.create("Sulfuras, Hand of Ragnaros", 1, 8)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 8 == items[0].quality

    def test_quality_doesnt_change_2(self):
        items = [ItemFactory.create("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 80 == items[0].quality


class TestAgedBrie:
    def test_name(self):
        items = [ItemFactory.create("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "Aged Brie" == items[0].name

    def test_sellin(self):
        items = [ItemFactory.create("Aged Brie", 1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].sell_in

    def test_sellin_negative(self):
        items = [ItemFactory.create("Aged Brie", -1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert -2 == items[0].sell_in

    def test_quality_before_sell_date(self):
        items = [ItemFactory.create("Aged Brie", 1, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 3 == items[0].quality

    def test_quality_on_sell_date(self):
        items = [ItemFactory.create("Aged Brie", 0, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 4 == items[0].quality

    def test_quality_after_sell_date(self):
        items = [ItemFactory.create("Aged Brie", -1, 4)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 6 == items[0].quality

    def test_quality_not_above_fifty(self):
        items = [ItemFactory.create("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

    def test_quality_not_above_fifty_2(self):
        items = [ItemFactory.create("Aged Brie", -2, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

    def test_quality_not_above_fifty_3(self):
        items = [ItemFactory.create("Aged Brie", -2, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality


class TestBackstage:
    def test_name(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "Backstage passes to a TAFKAL80ETC concert" == items[0].name

    def test_sellin(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].sell_in

    def test_sellin_negative(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", -1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert -2 == items[0].sell_in

    def test_quality_before_ten_days(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 11, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 1 == items[0].quality

    def test_quality_on_ten_days(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 10, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 4 == items[0].quality

    def test_quality_after_ten_days(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 6, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 4 == items[0].quality

    def test_quality_on_five_days(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 5, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 5 == items[0].quality

    def test_quality_after_five_days(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 1, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 5 == items[0].quality

    def test_quality_on_concert_day(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 0, 4)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_after_concert(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", -1, 4)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_not_above_fifty(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 11, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

    def test_quality_not_above_fifty_2(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 6, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

    def test_quality_not_above_fifty_3(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

    def test_quality_not_above_fifty_4(self):
        items = [ItemFactory.create("Backstage passes to a TAFKAL80ETC concert", 2, 48)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality


class TestConjured:
    def test_name(self):
        items = [ItemFactory.create("Conjured Sword of Doom", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "Conjured Sword of Doom" == items[0].name

    def test_sellin(self):
        items = [ItemFactory.create("Conjured Sword of Doom", 1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].sell_in

    def test_sellin_negative(self):
        items = [ItemFactory.create("Conjured Sword of Doom", -1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert -2 == items[0].sell_in

    def test_quality_before_sell_date(self):
        items = [ItemFactory.create("Conjured Sword of Doom", 1, 3)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 1 == items[0].quality

    def test_quality_on_sell_date(self):
        items = [ItemFactory.create("Conjured Sword of Doom", 0, 6)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 2 == items[0].quality

    def test_quality_after_sell_date(self):
        items = [ItemFactory.create("Conjured Sword of Doom", -1, 6)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 2 == items[0].quality

    def test_quality_not_below_zero(self):
        items = [ItemFactory.create("Conjured Sword of Doom", 2, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_not_below_zero2(self):
        items = [ItemFactory.create("Conjured Sword of Doom", 2, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_not_below_zero3(self):
        items = [ItemFactory.create("Conjured Sword of Doom", -2, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_not_below_zero4(self):
        items = [ItemFactory.create("Conjured Sword of Doom", -2, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_not_below_zero5(self):
        items = [ItemFactory.create("Conjured Sword of Doom", -2, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_not_below_zero6(self):
        items = [ItemFactory.create("Conjured Sword of Doom", -2, 3)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality
