import time
from .message import Message # Reverted to intra-package import

def receive_message() -> Message:
    """
    Simulates receiving a message.
    """
    # Placeholder values for a simulated message
    sender_id = "user123"
    content = "Hello, this is a test message for platform_A!"
    timestamp = time.time()
    target_platform = "platform_A"  # Simulate a target platform
    return Message(sender_id, content, timestamp, target_platform)

def get_target_platform(message: Message) -> str:
    """
    Determines the target platform for the message.
    """
    # For now, directly use the message's target_platform attribute
    print(f"Routing message for platform: {message.target_platform}")
    return message.target_platform

def send_message_to_platform(message: Message, platform: str):
    """
    Simulates sending the message to the target platform.
    """
    print(f"Simulating sending message to {platform}:")
    print(f"  Sender: {message.sender_id}")
    print(f"  Content: {message.content}")
    print(f"  Timestamp: {message.timestamp}")
    print(f"Message sent to {platform}.")

def start_relay_service():
    """
    Starts the message relay service.
    """
    print("Message relay service started.")
    message = receive_message()
    print("Received message:")
    print(message)

    target_platform = get_target_platform(message)
    send_message_to_platform(message, target_platform)

if __name__ == "__main__":
    start_relay_service()
