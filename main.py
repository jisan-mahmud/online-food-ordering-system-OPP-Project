from abc import ABC, abstractmethod
class MenuItem(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abstractmethod
    def __str__(self):
        ...

class Drink(MenuItem):
    def __init__(self, name: str, price: int, size: str):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Size: {self.size}'

class Dishes(MenuItem):
    def __init__(self, name, price, ingredient):
        super().__init__(name, price, ingredient)

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Ingredient: {self.ingredient}'

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.__items = [] #add item in this list a dictionary formate

    def add_food(self, item, quantity):
        for item_info in self.__items:
            if item_info['item'] == item:
                item_info['quantity'] += quantity
                return
        self.__items.append({'item': item, 'quantity': quantity})
        print('Add a item succesfully!')

    def remove_food(self, item):
        for item_info in self.__items:
            if item_info['item'] == item:
                self.__items.remove(item_info)
                print('Remove this item from restaurant....')

    def display(self):
        print('-------------------------------')
        print('ALL AVAILABLE ITEMS:')
        for item_info in self.__items:
            print(item_info['item'], item_info['quantity'])


