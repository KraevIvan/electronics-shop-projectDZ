import pytest
from src.keyboard import Keyboard


@pytest.fixture
def kb():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_keyboard(kb):
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
    kb.language = 'CH'
    # # AttributeError: property 'language' of 'Keyboard' object has no setter
