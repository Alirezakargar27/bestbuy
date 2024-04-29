import pytest
from products import Product

def test_create_normal_product():
    product = Product("Test Product", price=10, quantity=20)
    assert product.name == "Test Product"
    assert product.price == 10
    assert product.quantity == 20
    assert product.is_active() == True

def test_create_invalid_product():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative Price

def test_product_inactive_when_quantity_zero():
    product = Product("Test Product", price=10, quantity=0)
    assert product.is_active() == False


def test_product_purchase():
    product = Product("Test Product", price=10, quantity=20)
    total_price = product.buy(5)
    assert product.quantity == 15
    assert total_price == 50

def test_buying_larger_quantity_invokes_exception():
    product = Product("Test Product", price=10, quantity=20)
    with pytest.raises(Exception):
        product.buy(25)  # Buying more than available quantity

# Additional tests can be added as needed
