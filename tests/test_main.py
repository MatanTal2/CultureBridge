import unittest
import time
from io import StringIO
from unittest.mock import patch

# Make sure src is in the path for imports
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.message import Message
from src.main import receive_message, get_target_platform, send_message_to_platform

class TestMessageRelay(unittest.TestCase):

    def test_message_creation(self):
        """Test Message class instantiation and attributes."""
        sender = "test_sender"
        content = "Hello Test"
        ts = time.time()
        platform = "test_platform"
        msg = Message(sender, content, ts, platform)
        self.assertEqual(msg.sender_id, sender)
        self.assertEqual(msg.content, content)
        self.assertEqual(msg.timestamp, ts)
        self.assertEqual(msg.target_platform, platform)
        self.assertIn(sender, str(msg))
        self.assertIn(content, str(msg))
        self.assertIn(platform, str(msg))

    def test_receive_message(self):
        """Test receive_message function."""
        # Allow some time difference for timestamp comparison
        time_before_call = time.time()
        msg = receive_message()
        time_after_call = time.time()

        self.assertIsInstance(msg, Message)
        self.assertEqual(msg.sender_id, "user123")
        # Using assertIn because the exact content string might be slightly different
        self.assertIn("Hello, this is a test message for platform_A!", msg.content)
        self.assertTrue(time_before_call <= msg.timestamp <= time_after_call)
        self.assertEqual(msg.target_platform, "platform_A")


    def test_get_target_platform(self):
        """Test get_target_platform function."""
        sender = "router_test"
        content = "Routing content"
        ts = time.time()
        platform = "platform_X"
        msg = Message(sender, content, ts, platform)
        
        # Capture print output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            determined_platform = get_target_platform(msg)
            self.assertEqual(determined_platform, platform)
            self.assertIn(f"Routing message for platform: {platform}", mock_stdout.getvalue())

    def test_send_message_to_platform(self):
        """Test send_message_to_platform function."""
        sender = "sender_test"
        content = "Sending content"
        ts = time.time()
        platform = "platform_Y"
        msg = Message(sender, content, ts, platform)

        # Capture print output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            send_message_to_platform(msg, platform)
            output = mock_stdout.getvalue()
            self.assertIn(f"Simulating sending message to {platform}", output)
            self.assertIn(f"Sender: {sender}", output)
            self.assertIn(f"Content: {content}", output)
            self.assertIn(f"Message sent to {platform}", output)

if __name__ == '__main__':
    unittest.main()
