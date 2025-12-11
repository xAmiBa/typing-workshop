def add_item_to_cart(
    cart: list[dict[str, str | float]], item: str, price: float
) -> list[dict[str, str | float]]:
    cart.append({"item": item, "price": price})
    return cart


def calculate_total(cart: list[dict[str, str | float]]) -> float:
    total: float = 0.0
    for item in cart:
        item_price = item["price"]
        assert isinstance(item_price, float)
        total += item_price
    return total


def find_item(
    cart: list[dict[str, str | float]], item_name: str
) -> dict[str, str | float] | None:
    """Find an item in the cart by name. Returns None if not found."""
    for item in cart:
        if item["item"] == item_name:
            return item
    return None


def get_cart_summary(cart: list[dict[str, str | float]]) -> str:
    """Get a summary of the cart."""
    item_count = len(cart)
    total = calculate_total(cart)
    return f"{item_count} items, total: ${total}"


# Usage
shopping_cart: list[dict[str, str | float]] = []
add_item_to_cart(shopping_cart, "Apple", 1.50)
add_item_to_cart(shopping_cart, "Banana", 0.75)

found = find_item(shopping_cart, "Apple")
print(get_cart_summary(shopping_cart))
