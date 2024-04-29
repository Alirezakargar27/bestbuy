class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.quantity > 0

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity_to_buy) -> float:
        if not self.is_active():
            raise Exception(f"{self.name} is not currently available")

        if quantity_to_buy <= 0:
            raise ValueError("Quantity to buy must be positive")

        if quantity_to_buy > self.quantity:
            raise Exception(f"Not enough stock available for {self.name}")

        total_price = self.price * quantity_to_buy
        self.quantity -= quantity_to_buy

        if self.quantity <= 0:
            self.deactivate()

        return total_price


