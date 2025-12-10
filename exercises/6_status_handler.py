from typing import Literal

OrderCompleted = Literal["delivered", "cancelled"]
OrderPending = Literal["pending", "processing", "shipped"]
OrderStatus = OrderCompleted | OrderPending


def set_order_status(order_id: str, status: OrderStatus) -> None:
    print(f"Order {order_id} status: {status}")


def can_cancel_order(status: OrderStatus) -> bool:
    """Check if an order can be cancelled based on status."""
    return status in ["pending", "processing"]


def get_next_status(current: OrderStatus) -> OrderStatus:
    """Get the next valid status."""
    if current == "pending":
        return "processing"
    elif current == "processing":
        return "shipped"
    elif current == "shipped":
        return "delivered"
    else:
        return "completed"


def handle_order(order_id: str, status: str) -> None:
    """Handle an order based on its status."""
    set_order_status(order_id, status)
    if can_cancel_order(status):
        print("Order can be cancelled")


# Usage
handle_order("ORD-001", "pending")
handle_order("ORD-002", "invalid_status")
next_status = get_next_status("pending")
