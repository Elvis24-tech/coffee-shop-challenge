import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_validation():
    coffee = Coffee("Cappuccino")
    assert coffee.name == "Cappuccino"
    
    with pytest.raises(TypeError):
        Coffee(123)
    
    with pytest.raises(ValueError):
        Coffee("Ab")

def test_coffee_orders_and_customers():
    coffee = Coffee("Cappuccino")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    order1 = Order(customer1, coffee, 5.0)
    order2 = Order(customer2, coffee, 4.5)
    
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.75
    assert set(customer.name for customer in coffee.customers()) == {"Alice", "Bob"}