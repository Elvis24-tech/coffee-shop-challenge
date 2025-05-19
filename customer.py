from order import Order
from coffee import Coffee

class Customer:
    _all_orders = [] 

    def __init__(self, name):
        self._name = None
        self.name = name  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be 1-15 characters")
        self._name = value

    def orders(self):
        return [order for order in Customer._all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        order = Order(self, coffee, price)
        return order