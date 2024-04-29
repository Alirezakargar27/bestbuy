from products import Product, PercentDiscount, SecondHalfPrice, ThirdOneFree
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
            store.show_all_products()

        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"\nTotal of {total_quantity} items in store")

        elif choice == "3":
            print("\nCreating an order...")
            all_products = store.products

            if not all_products:
                print("No products available for ordering.")
            else:
                print("\nAvailable Products:")
                for idx, product in enumerate(all_products, 1):
                    print(f"{idx}. {product.show()}")

                order_list = []
                while True:
                    try:
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
            print("Thank you for using the Store Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 4.")

if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        Product("Windows License", price=125, quantity=0),
        Product("Shipping", price=10, quantity=250)
    ]

    # Create promotion objects
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Assign promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = Store(product_list)
    start(best_buy)
