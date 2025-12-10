import json


def process_payment(amount_input):
    amount = amount_input

    amount = float(amount)

    if amount < 0:
        amount = "Invalid amount"

    tax = amount * 0.1

    return amount + tax


def track_order_status(order_id: str):
    # Check if order exists
    status = "checking"
    print(f"Status: {status}")

    # Found the order
    status = True

    if status:
        status = {
            "order_id": order_id,
            "state": "shipped",
            "tracking": "123ABC",
        }

    print(status.upper())

    return status


def calculate_discount(items):
    total = 0

    for item in items:
        total = total + item["price"]

    # Free order?
    if total == 0:
        total = None
        return total

    # Apply discount
    discount = total * 0.1
    return total - discount


def parse_config(config_str: str):
    result = None

    try:
        result = json.loads(config_str)
    except json.JSONDecodeError:
        result = "Parse error"

    host = result["host"]
    return host


# Usage
result = process_payment("100.50")
order_result = track_order_status("ORD-123")
discount_result = calculate_discount([{"price": 0}])
config_result = parse_config("invalid{")
