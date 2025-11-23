import unittest
from unittest.mock import MagicMock, patch

from EXP7.notification import UserNotifier, EmailClient, send_system_announcement


class TestUserNotifier(unittest.TestCase):
    def test_send_welcome_email_uses_email_client(self):
        # Arrange: create a mock EmailClient
        mock_client = MagicMock(spec=EmailClient)
        notifier = UserNotifier(mock_client)

        # Act
        notifier.send_welcome_email("user@example.com")

        # Assert: ensure send_email was called with correct arguments
        mock_client.send_email.assert_called_once_with(
            "user@example.com",
            "Welcome!",
            "Thanks for signing up.",
        )

    def test_send_password_reset_with_link(self):
        mock_client = MagicMock(spec=EmailClient)
        notifier = UserNotifier(mock_client)

        reset_link = "https://example.com/reset?token=abc123"
        notifier.send_password_reset("user@example.com", reset_link)

        mock_client.send_email.assert_called_once_with(
            "user@example.com",
            "Password Reset",
            f"Click here to reset your password: {reset_link}",
        )

    def test_email_client_raises_error(self):
        # Simulate failure in dependency using side_effect
        mock_client = MagicMock(spec=EmailClient)
        mock_client.send_email.side_effect = RuntimeError("SMTP down")

        notifier = UserNotifier(mock_client)

        with self.assertRaises(RuntimeError):
            notifier.send_welcome_email("user@example.com")


class TestSystemAnnouncement(unittest.TestCase):
    @patch("EXP7.notification.EmailClient")
    def test_send_system_announcement_uses_email_client(self, MockEmailClient):
        # Mock the EmailClient class itself
        instance = MockEmailClient.return_value  # this is the fake instance

        send_system_announcement("user@example.com", "Hello users!")

        # Ensure constructor was called once
        MockEmailClient.assert_called_once()

        # Ensure send_email on the instance was called correctly
        instance.send_email.assert_called_once_with(
            "user@example.com",
            "System Announcement",
            "Hello users!",
        )


if __name__ == "__main__":
    unittest.main()
