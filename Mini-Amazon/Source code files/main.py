from users import UserManager
from products import ProductCatalog
from cart import CartManager
from orders import OrderManager

def main():
    user_manager = UserManager()
    catalog = ProductCatalog()
    cart_manager = CartManager()
    order_manager = OrderManager()

    while True:
        print("\n--- Welcome ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            user_manager.register()

        elif choice == "2":
            user = user_manager.login()
            if user:
                store_menu(user, catalog, cart_manager, order_manager)
                
        elif choice == "3":
            break
        
        else:
            print("Invalid choice.")

def store_menu(username, catalog, cart_manager, order_manager):
    while True:
        print(f"\n--- Store ({username}) ---")
        print("1. Browse products")
        print("2. Search products")
        print("3. View cart")
        print("4. Add to cart")
        print("5. Remove from cart")
        print("6. Checkout")
        print("7. Order history")
        print("8. Logout")

        choice = input("Choose: ")

        if choice == "1":
            catalog.list_products()

        elif choice == "2":
            catalog.search()

        elif choice == "3":
            cart_manager.view_cart(username, catalog)

        elif choice == "4":
            product_id = input("Enter product ID: ")
            product = catalog.get_product(product_id)

            if not product:
                print("Product not found.")
                continue

            try:
                qty = int(input("Quantity: "))
            except:
                print("Invalid input.")
                continue

            cart_manager.add_item(username, product, qty)

        elif choice == "5":
            cart_manager.remove_item(username)
        
        elif choice == "6":
            order_manager.checkout(username, cart_manager, catalog)

        elif choice == "7":
            order_manager.view_orders(username)

        elif choice == "8":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()