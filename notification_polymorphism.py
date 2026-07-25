class Notification:
    def send(self, message):
        raise NotImplementedError("This method should be overridden by subclasses.")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email notification: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS notification: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending push notification: {message}")

class WhatsappNotification(Notification):
    def send(self, message):
        print(f"Sending WhatsApp notification: {message}")

class DiscordNotification(Notification):
    def send(self, message):
        print(f"Sending Discord notification: {message}")

notifications = [EmailNotification(), SMSNotification(), PushNotification(), WhatsappNotification(), DiscordNotification()]
for notification in notifications:
    notification.send("Hello, this is a test notification!")
