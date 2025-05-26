import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture(autouse=True)
def clear_orders():
    Order._all_orders.clear()

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("a" * 16)
    c = Customer("Waititu")
    assert c.name == "Waititu"

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

def test_create_order_links_customer():
    waititu = Customer("Waititu")
    latte = Coffee("Latte")
    order = waititu.create_order(latte, 4.5)
    assert order.customer is waititu
    assert order.coffee is latte

def test_most_aficionado():
    waititu = Customer("Waititu")
    asuva = Customer("Asuva")
    latte = Coffee("Latte")
    assert Customer.most_aficionado(latte) is None
    waititu.create_order(latte, 4.0)
    asuva.create_order(latte, 6.0)
    waititu.create_order(latte, 2.0)
    assert Customer.most_aficionado(latte) == asuva
    waititu.create_order(latte, 10.0)
    assert Customer.most_aficionado(latte) == waititu