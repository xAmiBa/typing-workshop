def greet(name: str) -> str:
    return f"Hello, {name}!"


def get_age() -> int:
    age = int("25")
    return age


def create_welcome_message(name: str, age: int) -> str:
    greeting: str = greet(name)
    return greeting + f" You are {age} years old."


def count_characters(text: str) -> int:
    return len(text)


# Usage
message = create_welcome_message("Alice", get_age())
char_count = count_characters(message)
print(message)
print(f"Characters: {char_count}")
