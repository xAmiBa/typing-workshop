from typing import Any


def process_user_data(data: Any) -> str:
    name = data["name"]
    age = data["age"]
    return f"{name} is {age} years old"


def calculate_total(items: Any) -> float:
    total = 0.0
    for item in items:
        total += item["price"]
    return total


def find_user(users: Any, user_id: int) -> Any:
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def dangerous_any_example(value: Any) -> int:
    # Mypy won't complain about this, but it will crash if value is a string!
    return value * 2


# Usage
result1 = process_user_data("not a dict")
result2 = calculate_total({"item": "wrong type"})
result3 = find_user(None, 123)
result4 = dangerous_any_example("hello")
