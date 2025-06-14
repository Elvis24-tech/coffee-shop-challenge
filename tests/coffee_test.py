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

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")
    c = Coffee("Latte")
    assert c.name == "Latte"

def test_coffee_orders_and_customers():
    waititu = Customer("Waititu")
    asuva = Customer("Asuva")
    latte = Coffee("Latte")
    mocha = Coffee("Mocha")
    o1 = waititu.create_order(latte, 3.0)
    o2 = waititu.create_order(mocha, 4.0)
    o3 = asuva.create_order(latte, 5.0)
    assert set(latte.orders()) == {o1, o3}
    assert set(latte.customers()) == {waititu, asuva}

def test_num_orders_and_average_price():
    waititu = Customer("Waititu")
    asuva = Customer("Asuva")
    latte = Coffee("Latte")
    assert latte.num_orders() == 0
    assert latte.average_price() == 0
    waititu.create_order(latte, 4.0)
    asuva.create_order(latte, 6.0)
    assert latte.num_orders() == 2
    assert latte.average_price() == 5.0