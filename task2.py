class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Aged Brie item, increases in Quality the older it gets
            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality += 1
                item.sell_in = item.sell_in - 1
                # Once the sell by date has passed, Quality degrades twice as fast
                if item.sell_in < 0 and item.quality < 50:
                    item.quality = item.quality + 1
            #Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but, Quality drops to 0 after the concert
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    item.quality += 1
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality += 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality += 1
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality = 0
            # legendary item, never has to be sold or decreases in Quality
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            # Handle conjured items, degrade in Quality twice as fast as normal items
            elif item.name == "Conjured":
                if item.quality > 1: # was 0 but i change it to 1 so it wouldn't be less than 0
                    item.quality -= 2
                else:
                    item.quality = 0
                item.sell_in -= 1
                if item.sell_in < 0:
                    if item.quality > 1:# was 0 but i change it to 1 so it wouldn't be less than 0
                        item.quality -= 2
                    else:
                        item.quality = 0
            # normal item
            else:
                if item.quality > 0:
                    item.quality -= 1
                item.sell_in -= 1
                if item.sell_in < 0:
                    if item.quality > 0:
                        item.quality -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
