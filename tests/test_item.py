"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


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
    assert Item.all == [{"name": "samsung", "price": 20000, "quantity": 4}]


def test_repr(phone):
    assert phone.__repr__() == "name: samsung, price: 20000, quantity: 4"


def test_calculate_total_price(phone):
    assert phone.calculate_total_price() == 80000


def test_apply_discount(pay_rate_test):
    phone_test = pay_rate_test
    phone_test.apply_discount()
    assert phone_test.price == 16000
