# Coffee Shop Challenge

## Overview
The Coffee Shop Challenge is a Python project that simulates a coffee shop's ordering system. It includes models for customers, coffee types, and orders, along with methods to manage and retrieve information about them.

## Project Structure
```
coffee-shop-challenge
├── models
│   ├── __init__.py
│   ├── customer.py
│   ├── coffee.py
│   └── order.py
├── tests
│   ├── __init__.py
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
├── main.py
└── README.md
```

## Models
- **Customer**: Represents a customer with a name and methods to manage their orders.
- **Coffee**: Represents a coffee type with a name and methods to manage orders related to that coffee.
- **Order**: Represents an order made by a customer for a specific coffee at a certain price.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd coffee-shop-challenge
   ```
3. Install any required dependencies (if applicable).

## Usage
- Import the models in your Python scripts to create customers, coffees, and orders.
- Use the provided methods to manage and retrieve information about orders and customers.

## Running Tests
To run the tests, navigate to the `tests` directory and execute:
```
python -m unittest discover
```

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.