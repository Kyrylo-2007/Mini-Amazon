from storage import load_data, save_data
from datetime import datetime

ORDERS_FILE = "data/orders.json"

class OrderManager:
    def __init__(self):
        self.orders = load_data(ORDERS_FILE, [])

    def save(self):
        save_data(ORDERS_FILE, self.orders)

    def generate_order_id(self):
        return f"O{len(self.orders)+1:04d}"
    
    def checkout(self, username, cart_manager, catalog):
        cart = cart_manager.get_cart(username)

        if not cart:
            print("Cart is empty.")
            return
        
        total = 0
        items = []

        for item in cart:
            product = catalog.get_product(item["product_id"])
            if not product or item["qty"] > product["stock"]:
                print(f"Stock issue with {item['product_id']}")
                return
            
        for item in cart:
            product = catalog.get_product(item["product_id"])
            catalog.update_stock(product["product_id"], item["qty"])

            items.append({
                "product_id": product["product_id"],
                "qty": item["qty"],
                "unit_price": product["price"]
            })

            total += item["qty"] * product["price"]

        order = {
            "order_id": self.generate_order_id(),
            "username": username,
            "items": items,
            "total": total,
            "timestamp": str(datetime.now())
        }

        self.orders.append(order)
        self.save()

        cart_manager.carts[username] = []
        cart_manager.save()

        print("\nOrder placed successfully!")
        print(order)

    def view_orders(self, username):
        print("\n--- Order History: ---")
        for order in self.orders:
            if order["username"] == username:
                print(order)