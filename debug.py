from customer import Customer
from coffee import Coffee
from order import Order

def main():
    alice = Customer("Alice")
    bob = Customer("Bob")
    cappuccino = Coffee("Cappuccino")
    espresso = Coffee("Espresso")

    order1 = alice.create_order(cappuccino, 5.0)
    order2 = alice.create_order(espresso, 3.5)
    order3 = bob.create_order(cappuccino, 4.5)


    print(f"Alice's orders: {len(alice.orders())}")
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
    print(f"Cappuccino's order count: {cappuccino.num_orders()}")
    print(f"Cappuccino's average price: {cappuccino.average_price():.2f}")

if __name__ == "__main__":
    main()