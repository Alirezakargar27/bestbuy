from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * (1 - self.percent / 100)
        return discounted_price * quantity

class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * 0.5
        return discounted_price * quantity

class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        num_free = quantity // 3
        total_price = (quantity - num_free) * product.price
        return total_price

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self):
        return self.quantity > 0

    def activate(self):
        self.quantity = 0

    def deactivate(self):
        self.quantity = 0

    def show(self):
        if self.promotion:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {self.promotion.name}"
        else:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: None"

    def buy(self, quantity_to_buy):
        if not self.is_active():
            raise Exception(f"{self.name} is not currently available")

        if quantity_to_buy <= 0:
            raise ValueError("Quantity to buy must be positive")

        if quantity_to_buy > self.quantity:
            raise Exception(f"Not enough stock available for {self.name}")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity_to_buy)
        else:
            total_price = self.price * quantity_to_buy

        self.quantity -= quantity_to_buy

        if self.quantity <= 0:
            self.deactivate()

        return total_price

    def set_promotion(self, promotion):
        self.promotion = promotion