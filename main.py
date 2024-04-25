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

class Customer:
    __count = 0
    def __init__(self, name, address):
        self.__id = self.__count + 1
        Customer.__count += 1
        self.name = name
        self.address = address
        self.__order_history = [] # store all ordered history in list as a dictionary formate

    def get_id(self):
        return self.__id

    def order(self, item_dict):
        self.__order_history.append(item_dict)




class Restaurant:
    __restaurant_list = []
    __total_restaurant = 0
    def __init__(self, name):
        self.name = name
        self.__id = Restaurant.__total_restaurant + 1 # Generate id for restaurant
        Restaurant.__total_restaurant += 1 #increase total number of restaurant
        self.__items = [] #add item in this list a dictionary formate
        self.__customer = []
        self.__order_history = [] # store all ordered history in list as a dictionary formate
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

    def sign_up(self, customer_info):
        if customer_info in self.__customer:
            print('Customer already signup.')
        else:
            self.__customer.append(customer_info)
            print('Account create succefully...')

    def get_user(self, id: int):
        for curstomer in self.__customer:
            if curstomer.get_id() == id:
                return curstomer
        return False

    def order(self,restaurant, customer_id: int, item_id: int, quantity: int):
        customer = self.get_user(customer_id)
        if customer:
            for item_info in self.__items:
                if item_info['quantity'] < quantity:
                    print('Not enough item')
                elif item_info['item'].get_id() == item_id:
                    item_dict = {
                        "item_id": item_id,
                        "customer_id": customer_id,
                        "name": item_info['item'].name,
                        "price": item_info['item'].price,
                        "total_price": item_info['item'].price * quantity,
                        "quantity": quantity,
                    }
                    customer.order(item_dict)
                    self.__order_history.append(item_dict)
                    #decreament item quantity
                    item_info['quantity'] -= 1
                    if item_info['quantity'] < 1:
                        self.__items.remove(item_info)
                    print('Ordered Succsefully!\n', item_dict)
                    return
            print('Invalid item id...')
        else:
            print('Invalid Customer id...')


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
                print('4. Signup')
                print('5. Orderd a food item')
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
                    elif item_type == '2':
                        name = input('Enter drink name: ')
                        price = int(input('Enter drink price: '))
                        ingredient = input('Enter ingredient: ')
                        quantity = int(input('Enter drinks quantity: '))
                        dishe = Dishes(name, price, ingredient)
                        restaurant.add_food(dishe, quantity)
                elif user_choices == '2':
                    restaurant.view_items()
                elif user_choices == '3':
                    item_id = int(input('Enter item ID code: '))
                    restaurant.remove_food(item_id)
                elif user_choices == '4':
                    name = input('Enter your full name: ')
                    address = input('Enter your address: ')
                    user = Customer(name, address)
                    restaurant.sign_up(user)
                elif user_choices == '5':
                    customer_id = int(input('Enter customer id: '))
                    item_id = int(input('Enter item id code: '))
                    quantity = int(input('Enter Quantity: '))
                    restaurant.order(restaurant, customer_id, item_id, quantity)
                else:
                    'Choice a valid number...'
        else:
            print('Restaurant not found')