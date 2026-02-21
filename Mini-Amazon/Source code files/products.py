from storage import load_data, save_data

PRODUCTS_FILE = "data/products.json"

class ProductCatalog:
    def __init__(self):
        self.products = load_data(PRODUCTS_FILE, [])

    def save(self):
        save_data(PRODUCTS_FILE, self.products)

    def list_products(self):
        print("\n--- Products: ---")
        for p in self.products:
            print(f"{p['product_id']} | {p['name']} | ${p['price']} | Stock: {p['stock']}")
    
    def search(self):
        keyword = input("Search keyword: ").lower()
        results = [p for p in self.products if keyword in p["name"].lower()]

        if not results:
            print("No products found.")
            return
        
        for p in results:
            print(f"{p['product_id']} | {p['name']} | ${p['price']} | Stock: {p['stock']}")

    def get_product(self, product_id):
        for p in self.products:
            if p["product_id"] == product_id:
                return p
        return None
    
    def update_stock(self, product_id, qty):
        product = self.get_product(product_id)
        if product:
            product["stock"] -= qty
            self.save()