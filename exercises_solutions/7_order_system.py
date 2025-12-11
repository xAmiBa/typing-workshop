from typing import TypedDict


class OrderItem(TypedDict):
    product_name: str
    quantity: int
    price: float
    discount: float


class Order(TypedDict):
    order_id: str
    customer_name: str
    items: list[OrderItem]
    total: float


def create_order_item(name: str, qty: int, price: float) -> OrderItem:
    """Create an order item."""
    return {
        "product_name": name,
        "quantity": qty,
        "price": price,
        "discount": 0.0,
    }


def calculate_item_total(item: OrderItem) -> float:
    """Calculate total for an item."""
    return item["quantity"] * item["price"]


def create_order(order_id: str, customer: str) -> Order:
    """Create a new order."""
    return {"order_id": order_id, "customer_name": customer, "items": [], "total": 0.0}


def add_item_to_order(order: Order, item: OrderItem) -> None:
    """Add an item to an order."""
    order["items"].append(item)
    order["total"] += calculate_item_total(item)


# Usage
item = create_order_item("Widget", 2, 19.99)
order = create_order("ORD-001", "Alice")
add_item_to_order(order, item)
