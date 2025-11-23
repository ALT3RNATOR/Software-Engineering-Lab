"""
notification.py

Example module for EXP7 showing:
- dependency injection
- mocking with unittest.mock
"""

from dataclasses import dataclass


@dataclass
class EmailClient:
    """Simple email client dependency.

    In a real app, this would talk to an SMTP server or external API.
    Here we only simulate its interface for testing with mocks.
    """

    sender_address: str = "no-reply@example.com"

    def send_email(self, to: str, subject: str, body: str) -> None:
        """Send an email.

        In production code this would send a real email.
        For testing, we will **mock** this method.
        """
        print(f"Sending email to {to}: {subject}\n{body}")


class UserNotifier:
    """Service that sends emails to users.

    Uses dependency injection: an EmailClient instance is passed
    into the constructor instead of being created inside.
    """

    def __init__(self, email_client: EmailClient) -> None:
        self.email_client = email_client

    def send_welcome_email(self, user_email: str) -> None:
        """Send a welcome email to a new user."""
        subject = "Welcome!"
        body = "Thanks for signing up."
        self.email_client.send_email(user_email, subject, body)

    def send_password_reset(self, user_email: str, reset_link: str) -> None:
        """Send password reset email."""
        subject = "Password Reset"
        body = f"Click here to reset your password: {reset_link}"
        self.email_client.send_email(user_email, subject, body)


def send_system_announcement(to_email: str, message: str) -> None:
    """Function-style API that creates its own EmailClient internally.

    We'll use unittest.mock.patch to replace EmailClient here in tests.
    """
    client = EmailClient()
    client.send_email(to_email, "System Announcement", message)
