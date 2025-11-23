# EXP7 – Mocking and Dependency Injection

This experiment demonstrates:

- **Dependency Injection**:
  - `UserNotifier` receives an `EmailClient` instance via its constructor.
- **Mocking with unittest.mock**:
  - `MagicMock` used to fake `EmailClient` in tests.
  - `side_effect` used to simulate errors from dependencies.
  - `@patch("EXP7.notification.EmailClient")` used to replace the EmailClient class for testing `send_system_announcement()`.

Files:
- `notification.py` – main code (EmailClient, UserNotifier, send_system_announcement)
- `test_notification.py` – unit tests using unittest + unittest.mock
