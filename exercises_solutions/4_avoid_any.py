from typing import Any


def process_user_data(data: dict[str, str | int]) -> str:
    name = data["name"]
    age = data["age"]
    return f"{name} is {age} years old"


def calculate_total(items: list[dict[str, str | int]]) -> float:
    total: float = 0.0
    for item in items:
        item_price = item.get("price")
        if not isinstance(item_price, float):
            pass
        else:
            total += item_price
    return total


def find_user(users: Any, user_id: int) -> Any:
    for user in users:
        if user["id"] == user_id:
            return user
    return None


# Usage
result1 = process_user_data({"name": "Amina", "age": 30})
result2 = calculate_total([{"item": "wrong type"}])
result3 = find_user(None, 123)
