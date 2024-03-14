from src.item import Item
from src.keyboard_language import KeyboardLanguage


class Keyboard(Item, KeyboardLanguage):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        KeyboardLanguage.__init__(self)

    def __repr__(self):
        return f"{Item.__repr__(self)[:-1]}, {self.language})"
