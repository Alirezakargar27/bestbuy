from products import Product
from store import Store

def start(store):
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            # List all products in store
            print("\nList of all products in store:")
            all_products = store.get_all_products()
            if not all_products:
                print("No products available.")
            else:
                for idx, product in enumerate(all_products, 1):
                    print(f"{idx}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

        elif choice == "2":
            # Show total quantity of all products in store
            total_quantity = store.get_total_quantity()
            print(f"\nTotal of {total_quantity} items in store")

        elif choice == "3":
            # Make an order
            print("\nCreating an order...")
            all_products = store.get_all_products()

            if not all_products:
                print("No products available for ordering.")
            else:
                print("\nAvailable Products:")
                for idx, product in enumerate(all_products, 1):
                    print(f"{idx}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

                order_list = []
                while True:
                    try:
                        # Prompt user to choose a product for ordering
                        print("Enter the product number you want to order (or 'done' to finish):")
                        product_number = input("Product # (or 'done'): ")
                        if product_number.lower() == "done":
                            break

                        product_index = int(product_number) - 1
                        if 0 <= product_index < len(all_products):
                            selected_product = all_products[product_index]
                            quantity = int(input(f"How many units of '{selected_product.name}' do you want to order? "))
                            if quantity > selected_product.quantity:
                                print("Not enough stock available for this product.")
                            else:
                                order_list.append((selected_product, quantity))
                        else:
                            print("Invalid product number. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid product number.")

                if order_list:
                    total_price = store.order(order_list)
                    print(f"Order placed successfully! Total price: ${total_price:.2f}")

        elif choice == "4":
            # Quit
            print("Thank you for using the Store Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 4.")

if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    # Create a Store object with the initial inventory
    best_buy = Store(product_list)

    # Start the user interface
    start(best_buy)
