import pytest
from task2 import Item, GildedRose
from assertpy import soft_assertions

@pytest.mark.parametrize("expected", [
    {"name": "normal item", "sell_in": 10, "quality": 10},
    {"name": "Aged Brie", "sell_in": 10, "quality": 10},
    {"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 10, "quality": 10},
    {"name": "Sulfuras, Hand of Ragnaros", "sell_in": 10, "quality": 80},
    {"name": "Conjured", "sell_in": 10, "quality": 10}
])
def test_items_init(expected):
    actual_item = Item(expected.get("name"), expected.get("sell_in"), expected.get("quality"))

    _validate_results(actual=actual_item, expected=expected)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "normal item", "sell_in": 10, "quality": 10}, {"sell_in": 9, "quality": 9}),
])
def test_normal_item(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "normal item", "sell_in": -1, "quality": 10}, {"sell_in": -2, "quality": 8}),
])
# could rm cause checked in next test
def test_normal_item_quality_degrades_twice_as_fast_after_sell_by_date(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "normal item", "sell_in": 0, "quality": 10}, {"sell_in": -1, "quality": 8}),
    pytest.param({"name": "Aged Brie", "sell_in": 0, "quality": 10}, {"sell_in": -1, "quality": 12}),
    pytest.param({"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 0, "quality": 10},
                 {"sell_in": -1, "quality": 0}),
    pytest.param({"name": "Sulfuras, Hand of Ragnaros", "sell_in": 0, "quality": 80}, {"sell_in": 0, "quality": 80}),
    pytest.param({"name": "Conjured", "sell_in": 0, "quality": 10}, {"sell_in": -1, "quality": 6})
])
def test_quality_degrades_twice_as_fast_after_sell_by_date(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)


@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "normal item", "sell_in": 10, "quality": 0}, {"sell_in": 9, "quality": 0}),
])
def test_normal_item_quality_is_never_negative(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "normal item", "sell_in": 10, "quality": 0}, {"sell_in": 9, "quality": 0}),
    pytest.param({"name": "Aged Brie", "sell_in": 10, "quality": 0}, {"sell_in": 9, "quality": 1}),
    pytest.param({"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 10, "quality": 0},
                 {"sell_in": 9, "quality": 2}),
    pytest.param({"name": "Sulfuras, Hand of Ragnaros", "sell_in": 10, "quality": 80}, {"sell_in": 10, "quality": 80}),
    pytest.param({"name": "Conjured", "sell_in": 10, "quality": 0}, {"sell_in": 9, "quality": 0})
])
def test_quality_is_never_negative(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "Aged Brie", "sell_in": 10, "quality": 50}, {"sell_in": 9, "quality": 50}),
])
def test_aged_brie_quality_is_never_above_50(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "normal item", "sell_in": 10, "quality": 50}, {"sell_in": 9, "quality": 49}),
    pytest.param({"name": "Aged Brie", "sell_in": 10, "quality": 50}, {"sell_in": 9, "quality": 50}),
    pytest.param({"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 10, "quality": 50},
                 {"sell_in": 9, "quality": 50}),
    pytest.param({"name": "Sulfuras, Hand of Ragnaros", "sell_in": 10, "quality": 80}, {"sell_in": 10, "quality": 80}),
    pytest.param({"name": "Conjured", "sell_in": 10, "quality": 50}, {"sell_in": 9, "quality": 48})
])
def test_quality_is_never_above_50(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "Aged Brie", "sell_in": 10, "quality": 10}, {"sell_in": 9, "quality": 11}),
])
def test_aged_brie_quality_increases_by_1(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "Sulfuras, Hand of Ragnaros", "sell_in": 10, "quality": 80}, {"sell_in": 10, "quality": 80}),
])
def test_sulfuras_quality_and_sell_in_do_not_change(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 11, "quality": 10}, {"sell_in": 10, "quality": 11}),
])
def test_backstage_pass_quality_increases_by_1_when_sell_in_is_more_than_10(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 10, "quality": 10}, {"sell_in": 9, "quality": 12}),
])
def test_backstage_pass_quality_increases_by_2_when_sell_in_is_10_or_less(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 5, "quality": 10}, {"sell_in": 4, "quality": 13}),
])
def test_backstage_pass_quality_increases_by_3_when_sell_in_is_5_or_less(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 0, "quality": 10}, {"sell_in": -1, "quality": 0}),
])
def test_backstage_pass_quality_drops_to_0_after_concert(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

@pytest.mark.parametrize("before, after", [
    pytest.param({"name": "Conjured", "sell_in": 10, "quality": 10}, {"sell_in": 9, "quality": 8}),
])
def test_conjured_pass_quality_degrade_twice_as_fast_as_normal_items(before, after):
    items = Item(name=before.get('name'), sell_in=before.get('sell_in'), quality=before.get('quality'))
    gilded_rose = GildedRose([items])
    gilded_rose.update_quality()

    _validate_results(actual=items, expected=after)

def _validate_results(actual, expected):
    with soft_assertions():
        assert actual.quality == expected.get('quality')
        assert actual.sell_in == expected.get('sell_in')
