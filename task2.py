class GildedRose(object):
    """init function for class GildedRose
    Parameters
    ----------
    items : list
        represents the List of all items
    max_quality : int
        The max quality per item except "Sulfuras" item which could be more than the max (default is 50)
    min_quality : int
        The min quality per item (default is 0)
    """
    def __init__(self, items:list):
        self.items = items
        self.max_quality:int = 50
        self.min_quality:int = 0

    """Check's if quality is above 50, if yes returns 50, o.w returns parameter quality

    Parameters
    ----------
    quality : int
        The quality of an item

    Returns
    -------
    int
        returns the quality of an item
    """
    def __check_quality_above_50(self, quality: int)->int:
        if quality > self.max_quality:
            return self.max_quality  
        else:
            return quality

    """Check's if quality is negative, if yes returns 0, o.w returns parameter quality

    Parameters
    ----------
    quality : int
        The quality of an item

    Returns
    -------
    int
        returns the quality of an item
    """
    def __check_quality_negative(self, quality: int)->int:
        if quality < self.min_quality:
            return self.min_quality 
        else:
            return quality

    
    """Updates the quality of item aged_brie, it actually increases in Quality the older it gets,Once the sell by date 
    has passed, Quality increases twice as fast

    Parameters
    ----------
    item_index : int
        The index of an item in items list

    """
    def __update_quality_aged_brie(self, item_index: int)->None:
        self.items[item_index].sell_in -= 1
        self.items[item_index].quality += 2 if self.items[item_index].sell_in < 0 else 1
        self.items[item_index].quality = self.__check_quality_above_50(self.items[item_index].quality)

    """Updates the quality of item \"Backstage passes to a TAFKAL80ETC concert\", like aged brie, increases in Quality 
    as its SellIn value approaches; Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or 
    less but Quality drops to 0 after the concert it actually increases in Quality the older it gets

    Parameters
    ----------
    item_index : int
        The index of an item in items list

    """
    def __update_quality_backstage(self, item_index: int)->None:
         # Quality increases by 1 when there are more than 10 days
        if self.items[item_index].sell_in > 10:
            self.items[item_index].quality += 1
        # Quality increases by 2 when there are 10 days or less
        elif self.items[item_index].sell_in > 5:
            self.items[item_index].quality += 2
        #  Quality increases by 3 when there are 5 days or less
        elif self.items[item_index].sell_in > 0:
            self.items[item_index].quality += 3
        # sell_in=0, Quality drops to 0 after the concert
        else:
            self.items[item_index].quality = 0
        self.items[item_index].sell_in -= 1
        self.items[item_index].quality = 0 if self.items[item_index].sell_in < 0 else self.items[item_index].quality
        self.items[item_index].quality = self.__check_quality_above_50(self.items[item_index].quality)

    """Updates the quality of 'normal' item or 'conjured' item , the quality of normal item degrades in 1 as its SellIn value approaches,
    and conjured item degrades in 2 as its SellIn value approaches.

    Parameters
    ----------
    item_index : int
        The index of an item in items list
    quality_degrade : int
        The degrades that should be done to the item quality

    """
    def __update_quality_degrade_cases(self, item_index: int, quality_degrade: int)->None:
        self.items[item_index].quality -= quality_degrade
        self.items[item_index].sell_in -= 1
        if self.items[item_index].sell_in < 0:
                self.items[item_index].quality -= quality_degrade
        self.items[item_index].quality = self.__check_quality_negative(self.items[item_index].quality)

    """Handle the Updates of quality for all items

    """
    def update_quality(self)->None:
        for index,item in enumerate(self.items):
            # Aged Brie item, increases in Quality the older it gets
            if item.name == "Aged Brie":
                self.__update_quality_aged_brie(item_index=index)
            #Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but, Quality drops to 0 after the concert
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.__update_quality_backstage(item_index=index)
            # legendary item, never has to be sold or decreases in Quality
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            # Handle conjured items, degrade in Quality twice as fast as normal items
            elif item.name == "Conjured":
                self.__update_quality_degrade_cases(item_index=index, quality_degrade=2)
            # normal item
            else:
                self.__update_quality_degrade_cases(item_index=index, quality_degrade=1)

class Item:
    """init function for class Item
    Parameters
    ----------
    name : str
        The name of the item
    sell_in : int
        The sell_in of the item
    quality : int
        The quality of the item
    """
    def __init__(self, name:str, sell_in:int, quality:int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    """ returns a more information-rich, or official, string representation of an object.
    """
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
