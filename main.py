from abc import ABC, abstractmethod
class MenuItem(ABC):
    cout = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__id = self.cout + 1
        MenuItem.cout += 1
    @abstractmethod
    def __str__(self):
        ...

    def get_id(self):
        return self.__id

class Drink(MenuItem):
    def __init__(self, name: str, price: int, size: str):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Size: {self.size} -- ID: {self.get_id()}'

class Dishes(MenuItem):
    def __init__(self, name, price, ingredient):
        super().__init__(name, price, ingredient)

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Ingredient: {self.ingredient} -- ID: {self.get_id()}'

class Restaurant:
    __restaurant_list = []
    __total_restaurant = 0
    def __init__(self, name):
        self.name = name
        self.__id = Restaurant.__total_restaurant + 1 # Generate id for restaurant
        Restaurant.__total_restaurant += 1 #increase total number of restaurant
        self.__items = [] #add item in this list a dictionary formate
        Restaurant.__restaurant_list.append(self)
        print('Restaurant Create Succefully...')

    @classmethod
    def display_restaurant(cls):
        for restaurant in cls.__restaurant_list:
            print(f'Restaurant name :{restaurant.name}, Id: {restaurant.__id}')

    @classmethod
    def current_restant(cls, id):
        for restaurant in cls.__restaurant_list:
           if restaurant.__id == id:
               return restaurant
        return False

    def add_food(self, item, quantity):
        for item_info in self.__items:
            if item_info['item'] == item:
                item_info['quantity'] += quantity
                return
        self.__items.append({'item': item, 'quantity': quantity})
        print('Add a item succesfully!')

    def view_items(self):
         for item_info in self.__items:
             print(f'Item name: {item_info["item"]}')

    def remove_food(self, item_id):
        for item_info in self.__items:
            if item_info['item'].get_id() == item_id:
                self.__items.remove(item_info)
                print('Remove this item from restaurant....')

    def display(self):
        print('-------------------------------')
        print('ALL AVAILABLE ITEMS:')
        for item_info in self.__items:
            print(item_info['item'], item_info['quantity'])


while True:
    print('\n---NOW YOU IN HOME PAGE---\n')
    print('1. Create a restaurant')
    print('2. View all restaurant')
    print('3. Visit a restaurant')
    print('0. Exit')

    user_choices = input('Choices a option: ')

    if user_choices == '0':
        exit()
    elif user_choices == '1':
        name = input('Enter a name for restaurant: ')
        restaurant = Restaurant(name)
    elif user_choices == '2':
        Restaurant.display_restaurant()

    elif user_choices == '3':
        restaurant_id = int(input('Enter a restaurant code (You want to visit): '))
        restaurant = Restaurant.current_restant(restaurant_id)
        if restaurant:
            while True:
                print(f'\n---CURRENTLY YOU VISIT {restaurant.name}----\n')
                print('1. Add a food item')
                print('2. View all items')
                print('3. Remove a food item')
                print('0. Back')
                user_choices = input('Choice a option: ')
                if user_choices == '0':
                    break
                elif user_choices == '1':
                    item_type = int(input('What you want you add 1. Drinks or 2. Dishes? (Select a number): '))
                    if item_type == 1:
                        name = input('Enter drink name: ')
                        price = int(input('Enter drink price: '))
                        size = input('Enter drink size (Small, Medium, Large): ')
                        quantity = int(input('Enter drinks quantity: '))
                        drink = Drink(name, price, size)
                        restaurant.add_food(drink, quantity)
                elif user_choices == '2':
                    restaurant.view_items()
                elif user_choices == '3':
                    item_id = int(input('Enter item ID code: '))
                    restaurant.remove_food(item_id)
        else:
            print('Restaurant not found')