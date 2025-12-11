def get_user_coordinates(user_id: int) -> tuple[float, float]:
    """Return user's latitude and longitude as a tuple."""
    return (51.5074, -0.1278)


def get_user_tags(user_id: int) -> set[str]:
    """Return unique tags for a user."""
    return {"python", "typing", "mypy"}


def count_words(text: str) -> dict[str, int]:
    """Count word frequencies in text."""
    words = text.lower().split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def get_rgb_color(color_name: str) -> tuple[int, int, int]:
    """Return RGB values for a color."""
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
    }
    return colors.get(color_name, (0, 0, 0))


def merge_tags(tags1: set[str], tags2: set[str]) -> set[str]:
    """Merge two sets of tags."""
    return tags1 | tags2


def get_user_info(user_id: int) -> dict[str, int | str | bool]:
    """Get user information as a dictionary."""
    return {
        "id": user_id,
        "name": "Alice",
        "age": 30,
        "active": True,
    }


def parse_coordinates(coord_string: str) -> tuple[float, ...]:
    """Parse coordinate string like '10.5,20.3' into tuple of floats."""
    parts = coord_string.split(",")
    return tuple(float(x) for x in parts)


def get_top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """Return top N most common words with their counts."""
    # Missing type parameters - list of tuples
    word_counts = count_words(text)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]


# Usage
coords = get_user_coordinates(1)
tags = get_user_tags(1)
word_freq = count_words("hello world hello")
rgb = get_rgb_color("red")
merged = merge_tags({"python", "java"}, {"python", "go"})
info = get_user_info(1)
parsed = parse_coordinates("1.5,2.3,4.8")
top = get_top_words("the quick brown fox jumps over the lazy dog", 2)
