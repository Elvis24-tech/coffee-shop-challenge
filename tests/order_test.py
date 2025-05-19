import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_validation():
    customer = Customer("Alice")
    coffee = Coffee("Cappuccino")
    order = Order(customer, coffee, 5.0)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    
    with pytest.raises(TypeError):
        Order("not a customer", coffee, 5.0)
    with pytest.raises(TypeError):
        Order(customer, "not a coffee", 5.0)
    with pytest.raises(TypeError):
        Order(customer, coffee, "5.0")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 10.5)