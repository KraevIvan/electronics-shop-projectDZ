import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты класса Item и дочерние от него")
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, path):

        if os.path.exists(path):
            with open(path, newline='\n') as csvfile:
                items = csv.reader(csvfile, delimiter=' ')
                first_str = 0
                for item in items:
                    if first_str == 0:
                        first_str = 1
                    else:
                        item = item[0].split(",")
                        if len(item) < 3:
                            raise InstantiateCSVError('Файл item\\.csv поврежден')
                        else:
                            Item(item[0], float(item[1]), int(item[2]))
        else:
            raise FileNotFoundError("По данному пути файл item.csv отсутствует")

    @staticmethod
    def string_to_number(string):
        return int(float(string))


class InstantiateCSVError(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message is None:
            return f'InstantiateCSVError'
        else:
            return f"InstantiateCSVError, {self.message}"

