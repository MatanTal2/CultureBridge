class Message:
    """
    Represents a message in the relay service.
    """
    def __init__(self, sender_id: str, content: str, timestamp: float, target_platform: str = "default"):
        self.sender_id = sender_id
        self.content = content
        self.timestamp = timestamp
        self.target_platform = target_platform

    def __str__(self):
        return f"Message from {self.sender_id} to {self.target_platform} at {self.timestamp}: {self.content}"
