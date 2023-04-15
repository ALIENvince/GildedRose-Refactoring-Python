class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


class ItemFactory():
    @staticmethod
    def create(name, sell_in, quality):
        if name == "Aged Brie":
            return Brie(name, sell_in, quality)
        if name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert":
            return Backstage(name, sell_in, quality)
        else:
            return Normal(name, sell_in, quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Normal(Item):
    def update(self):
        self.sell_in -= 1

        if self.quality == 0:
            return

        self.quality -= 1
        if self.sell_in < 0 and self.quality > 0:
            self.quality -= 1


class Brie(Item):
    def update(self):
        self.sell_in -= 1

        if self.quality == 50:
            return

        self.quality += 1
        if self.sell_in < 0 and self.quality < 50:
            self.quality += 1


class Sulfuras(Item):
    def update(self):
        pass


class Backstage(Item):
    def update(self):
        self.sell_in -= 1

        if self.sell_in < 0:
            self.quality = 0
            return

        if self.sell_in < 5 and self.quality < 50:
            self.quality += 1
        if self.sell_in < 10 and self.quality < 50:
            self.quality += 1
        if self.sell_in >= 0 and self.quality < 50:
            self.quality += 1
