class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_normal(self, item):
        item.sell_in -= 1

        if item.quality == 0:
            return

        item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

    def update_brie(self, item):
        item.sell_in -= 1

        if item.quality == 50:
            return

        item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

    def update_sulfuras(self, item):
        pass

    def update_backstage(self, item):
        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality = 0
            return

        if item.sell_in < 5 and item.quality < 50:
            item.quality += 1
        if item.sell_in < 10 and item.quality < 50:
            item.quality += 1
        if item.sell_in >= 0 and item.quality < 50:
            item.quality += 1

    def update_quality(self):
        for item in self.items:
            if item.name == "foo":
                return self.update_normal(item)
            if item.name == "Aged Brie":
                return self.update_brie(item)
            if item.name == "Sulfuras, Hand of Ragnaros":
                return self.update_sulfuras(item)
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                return self.update_backstage(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
