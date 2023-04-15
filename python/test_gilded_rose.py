from gilded_rose import Item, GildedRose


class TestNormalItem:
    def test_name(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "foo" == items[0].name

    def test_sellin(self):
        items = [Item("foo", 1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].sell_in

    def test_sellin_negative(self):
        items = [Item("foo", -1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert -2 == items[0].sell_in

    def test_quality_before_sell_date(self):
        items = [Item("foo", 1, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 1 == items[0].quality

    def test_quality_on_sell_date(self):
        items = [Item("foo", 0, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_after_sell_date(self):
        items = [Item("foo", -1, 4)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 2 == items[0].quality

    def test_quality_not_below_zero(self):
        items = [Item("foo", -2, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_not_below_zero2(self):
        items = [Item("foo", 2, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality


class TestSulfuras:
    def test_name(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "Sulfuras, Hand of Ragnaros" == items[0].name

    def test_sellin(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 1 == items[0].sell_in

    def test_sellin_negative(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -4, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert -4 == items[0].sell_in

    def test_quality_doesnt_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 8)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 8 == items[0].quality

    def test_quality_doesnt_change_2(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 80 == items[0].quality


class TestAgedBrie:
    def test_name(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "Aged Brie" == items[0].name

    def test_sellin(self):
        items = [Item("Aged Brie", 1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].sell_in

    def test_sellin_negative(self):
        items = [Item("Aged Brie", -1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert -2 == items[0].sell_in

    def test_quality_before_sell_date(self):
        items = [Item("Aged Brie", 1, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 3 == items[0].quality

    def test_quality_on_sell_date(self):
        items = [Item("Aged Brie", 0, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 4 == items[0].quality

    def test_quality_after_sell_date(self):
        items = [Item("Aged Brie", -1, 4)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 6 == items[0].quality

    def test_quality_not_above_fifty(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

    def test_quality_not_above_fifty_2(self):
        items = [Item("Aged Brie", -2, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

    def test_quality_not_above_fifty_3(self):
        items = [Item("Aged Brie", -2, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality


class TestBackstage:
    def test_name(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "Backstage passes to a TAFKAL80ETC concert" == items[0].name

    def test_sellin(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].sell_in

    def test_sellin_negative(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert -2 == items[0].sell_in

    def test_quality_before_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 1 == items[0].quality

    def test_quality_on_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 4 == items[0].quality

    def test_quality_after_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 4 == items[0].quality

    def test_quality_on_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 5 == items[0].quality

    def test_quality_after_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 5 == items[0].quality

    def test_quality_on_concert_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 4)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 4)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_quality_not_above_fifty(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

    def test_quality_not_above_fifty_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

    def test_quality_not_above_fifty_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

    def test_quality_not_above_fifty_4(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 48)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality

