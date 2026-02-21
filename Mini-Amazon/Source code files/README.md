###   Mini-Amazon   ###


# How to run the program #

1. Make sure Python 3 is installed on your system.
2. Download or clone the project folder.
3. Ensure the following structure exists:

Source code files/
│
├── main.py
├── users.py
├── products.py
├── cart.py
├── orders.py
├── storage.py
│
└── data/
    ├── users.json
    ├── products.json
    ├── carts.json
    └── orders.json

4. Open a terminal in the project directory and run:

python main.py

5. Use the menu:
  1. Register a new account;
  2. Login;
  3. Access store features.


# Features implemented: #

1. User System
  • User registration with unique username
  • Password validation (minimum length of 6 characters)
  • User login authentication
  • Persistent storage of user data

2. Product Catalog
  • View all available products
  • Search products by name (case-insensitive)
  • View product details (ID, name, price, stock)
  • Stock validation when adding to cart

3. Cart System
  • Add products to cart with quantity validation
  • Prevent adding more than available stock
  • Remove items from cart
  • View cart contents:
    • Product name
    • Quantity
    • Unit price
    • Subtotal
  • Display total cart value
  • Persistent cart storage per user

4. Checkout System
  • Re-validates stock before checkout
  • Deducts product stock after purchase
  • Generates order summary (receipt)
  • Clears cart after successful checkout
  • Saves order history

5. Order History
  • View all previous orders for a user
  • Each order includes:
    • Order ID
    • Username
    • Items purchased(Product ID, Quantity, Unit Price)
    • Total cost
    • Date and time


# How data is stored: #

The system uses JSON files for persistent storage. Data is saved and loaded automatically.

`users.json`
  Stores user credentials:

[
    {
        "username": "Alex",
        "password": "ALEX_2000"
    }
]


`products.json`
  Stores product catalog:

[
    {
        "product_id": "1",
        "name": "USB-C Cable",
        "price": 9.99,
        "stock": 30
    },
    {
        "product_id": "2",
        "name": "Wireless Mouse",
        "price": 19.99,
        "stock": 15
    },
    {
        "product_id": "3",
        "name": "iPhone 17 Pro Max",
        "price": 1099.99,
        "stock": 10
    },
    {
        "product_id": "4",
        "name": "iPad Pro 11 (M5)",
        "price": 999.99,
        "stock": 3
    },
    {
        "product_id": "5",
        "name": "MacBook Pro (M5)",
        "price": 1999.99,
        "stock": 20
    }
]


`carts.json`
  Stores user carts:

  {
    "Alex": [{"product_id": "4", "qty": 2}]
  }


`orders.json`
  Stores order history:

[
    {
        "order_id": "O0001",
        "username": "Alex",
        "items": [
            {
                "product_id": "4",
                "qty": 2,
                "unit_price": 999.99
            }
        ],
        "total": 1999.98,
        "timestamp": "2026-02-21 00:23:19.643567"
    }
]


# Known limitations: #
  • Passwords are stored in plain text (no hashing)
  • No graphical user interface (console-based only)
  • No database (uses JSON files instead)
  • No support for multiple users running simultaneously
  • Limited error messages for some edge cases
  • No admin panel for managing products