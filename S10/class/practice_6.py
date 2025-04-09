
class Email:
    def __init__(self, sender, recipients, subject, body):
        self.sender = sender
        self.recipients = recipients
        self.subject = subject
        self.body = body

    def send_email(self):
        print(f"Sending email from {self.sender} to {', '.join(self.recipients)}")
        print(f"Subject: {self.subject}")
        print(f"Body: {self.body}")


# Example usage
email = Email(
    sender="example@example.com",
    recipients=["recipient1@example.com", "recipient2@example.com"],
    subject="Meeting Reminder",
    body="Don't forget about the meeting tomorrow at 10 AM."
    )
email.send_email()