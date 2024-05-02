from typing import List, Tuple
from products import Product

class Store:
    def __init__(self, products: List[Product]):
        self.products = products  # List to hold all products in the store

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        active_products = [product for product in self.products if product.is_active()]
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except Exception as e:
                print(f"Error ordering {product.name}: {e}")
        return total_price

    def show_all_products(self):
        print("\nList of all products in store:")
        for product in self.products:
            print(product.show())