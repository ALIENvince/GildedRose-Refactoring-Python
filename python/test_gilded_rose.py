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

    def test_quality_decrease(self):
        items = [Item("foo", 1, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 1 == items[0].quality

    def test_quality_decrease_fast(self):
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
