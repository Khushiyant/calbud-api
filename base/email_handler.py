from django.core.mail import send_mail

class EmailHandler:
    def __init__(self, subject, message, recipient_list):
        self.subject = subject
        self.message = message
        self.from_email = "dummyt1024@gmail.com"
        self.recipient_list = recipient_list

    def send(self):
        send_mail(
            self.subject,
            self.message,
            self.from_email,
            self.recipient_list,
            fail_silently=False,
        )

if __name__ == "__main__":
    email = EmailHandler(
        "Test Email",
        "This is a test email",
        "diveshchauhan814@gmail.com"
        )
    email.send()