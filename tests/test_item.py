"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError


@pytest.fixture
def phone():
    samsung = Item("samsung", 20000, 4)
    return samsung


@pytest.fixture
def pay_rate_test(phone):
    phone_test = phone
    phone_test.pay_rate = 0.8
    return phone_test


def test_init(phone):
    assert phone.price == 20000
    assert phone.name == "samsung"
    assert phone.quantity == 4


def test_repr(phone):
    assert phone.__repr__() == "Item('samsung', 20000, 4)"


def test_str(phone):
    assert phone.__str__() == "samsung"


def test_calculate_total_price(phone):
    assert phone.calculate_total_price() == 80000


def test_apply_discount(pay_rate_test):
    phone_test = pay_rate_test
    phone_test.apply_discount()
    assert phone_test.price == 16000


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv('./src/items.csv')
    assert len(Item.all) == 5
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("./homework-3/item.csv")
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("./tests/items_for_tests.csv")


def test_name(phone):
    phone.name = 'Смартфон'
    assert phone.name == 'Смартфон'

    phone.name = 'СуперСмартфон'
    assert phone.name == "СуперСмарт"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_add(phone):
    phone2 = Item("iphone", 25000, 3)
    assert phone + phone2 == 7
    with pytest.raises(ValueError, match="Складывать можно только объекты класса Item и дочерние от него"):
        phone + 5


def test_instantiate_csv_error():
    assert str(InstantiateCSVError()) == 'InstantiateCSVError'
    assert str(InstantiateCSVError("ERROR")) == "InstantiateCSVError, ERROR"
