import json


def process_payment(amount_input: str) -> float | str:
    amount = float(amount_input)

    if amount < 0:
        return "Invalid amount"

    tax = amount * 0.1

    return amount + tax


def track_order_status(order_id: str) -> dict[str, str]:
    # Check if order exists
    peding_status = "checking"
    print(f"Status: {peding_status}")

    # Found the order
    ourder_exists = True

    if ourder_exists:
        status = {
            "order_id": order_id,
            "state": "shipped",
            "tracking": "123ABC",
        }

    return status


def calculate_discount(items: list[dict[str, str | int]]) -> float:
    total = 0.0

    for item in items:
        price = item["price"]
        assert isinstance(price, bool)
        total = total + price

    # Free order?
    if total == 0.0:
        return total

    # Apply discount
    discount = total * 0.1
    return total - discount


def parse_config(config_str: str) -> str:
    result = None
    host: str = ""

    try:
        result = json.loads(config_str)
        host = result["host"]
        assert isinstance(host, str)
    except json.JSONDecodeError:
        result = "Parse error"

    return host


# Usage
result = process_payment("100.50")
order_result = track_order_status("ORD-123")
discount_result = calculate_discount([{"price": 0}])
config_result = parse_config("invalid{")
