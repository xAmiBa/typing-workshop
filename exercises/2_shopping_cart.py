def add_item_to_cart(cart: list, item: str, price: float):
    cart.append({"item": item, "price": price})
    return cart


def calculate_total(cart: list) -> float:
    total = 0
    for item in cart:
        total += item["price"]
    return total


def find_item(cart: list, item_name: str) -> dict:
    """Find an item in the cart by name. Returns None if not found."""
    for item in cart:
        if item["item"] == item_name:
            return item
    return None


def get_cart_summary(cart: list) -> str:
    """Get a summary of the cart."""
    item_count = len(cart)
    total = calculate_total(cart)
    return f"{item_count} items, total: ${total}"


# Usage
shopping_cart: list = []
add_item_to_cart(shopping_cart, "Apple", 1.50)
add_item_to_cart(shopping_cart, "Banana", 0.75)

found = find_item(shopping_cart, "Apple")
print(get_cart_summary(shopping_cart))
