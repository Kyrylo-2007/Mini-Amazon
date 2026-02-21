from storage import load_data, save_data

CART_FILE = "data/carts.json"

class CartManager:
    def __init__(self):
        self.carts = load_data(CART_FILE, {})

    def save(self):
        save_data(CART_FILE, self.carts)

    def get_cart(self, username):
        return self.carts.setdefault(username, [])
    
    def add_item(self, username, product, qty):
        if qty <= 0:
            print("Invalid quantity.")
            return
        
        if qty > product["stock"]:
            print("Not enough stock!")
            return
        
        cart = self.get_cart(username)

        for item in cart:
            if item["product_id"] == product["product_id"]:
                item["qty"] += qty
                self.save()
                print("Updated cart.")
                return
            
        cart.append({"product_id": product["product_id"], "qty": qty})
        self.save()
        print("Item added to cart.")

    def remove_item(self, username):
        cart = self.get_cart(username)
        product_id = input("Enter product ID to remove: ")

        for item in cart:
            if item["product_id"] == product_id:
                cart.remove(item)
                self.save()
                print("Item removed.")
                return
        
        print("Item not found in cart.")

    def view_cart(self, username, catalog):
        cart = self.get_cart(username)
        total = 0

        print("\n--- Your Cart: ---")
        for item in cart:
            product = catalog.get_product(item["product_id"])
            if not product:
                continue

            subtotal = item["qty"] * product["price"]
            total += subtotal

            print(f"{product['name']} | Qty: {item['qty']} | ${product['price']} | Subtotal: ${subtotal}")

        print(f"Total: ${total}")