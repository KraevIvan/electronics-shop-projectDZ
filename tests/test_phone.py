import pytest
from src.phone import Phone


@pytest.fixture
def phone1():
    samsung = Phone("samsung", 20000, 4, 2)
    return samsung


def test_init(phone1):
    assert phone1.price == 20000
    assert phone1.name == "samsung"
    assert phone1.quantity == 4
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        assert Phone("Meizu", 25000, 3, -1) == ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
