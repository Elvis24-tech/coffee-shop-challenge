import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture(autouse=True)
def clear_orders():
    if hasattr(Order, "_all_orders"):
        Order._all_orders.clear()

def test_order_creation_and_properties():
    cust = Customer("Asuva")
    cof = Coffee("Mocha")
    order = Order(cust, cof, 5.0)
    assert order.customer is cust
    assert order.coffee is cof
    assert order.price == 5.0

def test_order_price_validation():
    cust = Customer("Asuva")
    cof = Coffee("Mocha")
    with pytest.raises(TypeError):
        Order(cust, cof, "expensive")
    with pytest.raises(ValueError):
        Order(cust, cof, 0.5)
    with pytest.raises(ValueError):
        Order(cust, cof, 20.0)

def test_coffee_num_orders_and_average_price():
    waititu = Customer("Waititu")
    asuva = Customer("Asuva")
    latte = Coffee("Latte")
    assert latte.num_orders() == 0
    assert latte.average_price() == 0
    waititu.create_order(latte, 4.0)
    asuva.create_order(latte, 6.0)
    assert latte.num_orders() == 2
    assert latte.average_price() == 5.0

def test_customer_orders_and_coffees():
    waititu = Customer("Waititu")
    asuva = Customer("Asuva")
    latte = Coffee("Latte")
    mocha = Coffee("Mocha")
    o1 = waititu.create_order(latte, 3.0)
    o2 = waititu.create_order(mocha, 4.0)
    o3 = asuva.create_order(latte, 5.0)
    assert set(waititu.orders()) == {o1, o2}
    assert set(waititu.coffees()) == {latte, mocha}
    assert set(latte.customers()) == {waititu, asuva}
    assert set(latte.orders()) == {o1, o3} 

def test_most_aficionado():
    waititu = Customer("Waititu")
    asuva = Customer("Asuva")
    latte = Coffee("Latte")
    mocha = Coffee("Mocha")
    assert Customer.most_aficionado(latte) is None
    waititu.create_order(latte, 4.0)
    asuva.create_order(latte, 6.0)
    waititu.create_order(latte, 2.0)
    assert Customer.most_aficionado(latte) == asuva
    waititu.create_order(latte, 10.0)
    assert Customer.most_aficionado(latte) == waititu
    assert Customer.most_aficionado(mocha) is None