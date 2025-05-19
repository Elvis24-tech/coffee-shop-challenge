import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    customer = Customer("Alice")
    assert customer.name == "Alice"
    
    with pytest.raises(TypeError):
        Customer(123)
    
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_customer_orders_and_coffees():
    customer = Customer("Bob")
    coffee1 = Coffee("Cappuccino")
    coffee2 = Coffee("Espresso")
    order1 = customer.create_order(coffee1, 5.0)
    order2 = customer.create_order(coffee2, 3.5)
    
    assert len(customer.orders()) == 2
    assert set(coffee.name for coffee in customer.coffees()) == {"Cappuccino", "Espresso"}
