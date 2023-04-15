class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


DAY = 1
QUALITY_UNIT = 1
TODAY = 0
MIN_QUALITY = 0
MAX_QUALITY = 50

BACKSTAGE_CLOSE = 10
BACKSTAGE_VERY_CLOSE = 5


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Normal(Item):
    def update(self):
        self.sell_in -= DAY

        if self.quality == MIN_QUALITY:
            return

        self.quality -= QUALITY_UNIT
        if self.sell_in < TODAY and self.quality > MIN_QUALITY:
            self.quality -= QUALITY_UNIT


class Brie(Item):
    def update(self):
        self.sell_in -= DAY

        if self.quality == MAX_QUALITY:
            return

        self.quality += QUALITY_UNIT
        if self.sell_in < TODAY and self.quality < MAX_QUALITY:
            self.quality += QUALITY_UNIT


class Sulfuras(Item):
    def update(self):
        pass


class Backstage(Item):
    def update(self):
        self.sell_in -= DAY

        if self.sell_in < TODAY:
            self.quality = MIN_QUALITY
            return

        if self.sell_in < BACKSTAGE_VERY_CLOSE and self.quality < MAX_QUALITY:
            self.quality += QUALITY_UNIT
        if self.sell_in < BACKSTAGE_CLOSE and self.quality < MAX_QUALITY:
            self.quality += QUALITY_UNIT
        if self.sell_in >= TODAY and self.quality < MAX_QUALITY:
            self.quality += QUALITY_UNIT


ITEMS_DICT = {
        "Aged Brie": Brie,
        "Sulfuras, Hand of Ragnaros": Sulfuras,
        "Backstage passes to a TAFKAL80ETC concert": Backstage
        }


class ItemFactory():
    @staticmethod
    def create(name, sell_in, quality):
        if name in ITEMS_DICT:
            return ITEMS_DICT[name](name, sell_in, quality)
        return Normal(name, sell_in, quality)


