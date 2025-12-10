from typing import Callable
from dataclasses import dataclass


@dataclass
class Message:
    sender: str
    content: str
    msg_type: str


def validate_messages(
    messages: list[Message],
    validator: Callable[[Message], str],
) -> list[Message]:
    """Filter messages using a validation function."""
    return [msg for msg in messages if validator(msg)]


def format_messages(
    messages: list[Message],
    formatter,  # Error: Missing Callable type!
) -> list[str]:
    """Format messages using a formatter function."""
    return [formatter(msg) for msg in messages]


def send_message_with_callback(
    message: Message, send_handler: Callable[[Message], None]
) -> None:
    """Send a message and get confirmation."""
    confirmation = send_handler(message)
    # Error: send_handler returns None, but we're trying to use it!
    print(f"Sent with confirmation: {confirmation}")


def apply_spam_filter(
    messages: list[Message], is_spam: Callable[[Message], bool]
) -> tuple[list[Message], list[Message]]:
    """Separate messages into spam and legitimate using spam detector."""
    legitimate = []
    spam = []
    for msg in messages:
        if is_spam(msg):
            spam.append(msg)
        else:
            legitimate.append(msg)
    return legitimate, spam


def create_message_pipeline(
    validator: Callable[[str], bool], transformer: Callable[[str], str]
) -> Callable[[str], str]:
    """
    Create a pipeline that validates then transforms message content.
    Error: Wrong return type - should return str | None
    """

    def pipeline(content: str) -> str:
        if validator(content):
            return transformer(content)
        return None  # Error: Returns None but annotation says str

    return pipeline


def notify_on_keyword(
    messages: list[Message], keyword: str, notifier: Callable[[Message], None]
) -> int:
    """Notify for each message containing keyword. Return count."""
    count = 0
    for msg in messages:
        if keyword.lower() in msg.content.lower():
            notifier(msg)
            count += 1
    return count


# Usage examples
messages = [
    Message("alice@example.com", "Hello world", "email"),
    Message("spam@bad.com", "BUY NOW!!!", "email"),
    Message("+44123456", "Meeting at 3pm", "sms"),
]


# Validators
def is_valid_email(msg: Message) -> bool:
    return "@" in msg.sender and len(msg.content) > 0


def is_spam_message(msg: Message) -> bool:
    spam_words = ["BUY NOW", "CLICK HERE", "FREE MONEY"]
    return any(word in msg.content.upper() for word in spam_words)


# Formatters
def format_for_display(msg: Message) -> str:
    return f"From {msg.sender}: {msg.content}"


def send_email(msg: Message) -> None:
    print(f"Sending email to {msg.sender}")


# This should cause errors:
valid_msgs = validate_messages(messages, is_valid_email)
formatted = format_messages(messages, format_for_display)
send_message_with_callback(messages[0], send_email)
legitimate, spam = apply_spam_filter(messages, is_spam_message)

# Pipeline
pipeline = create_message_pipeline(lambda s: len(s) > 0, lambda s: s.upper())
result = pipeline("hello")
