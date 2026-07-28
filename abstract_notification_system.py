from abc import ABCMeta, abstractmethod

class Notification(metaclass=ABCMeta):
  @abstractmethod
  def send(self,message):
    pass

class EmailNotification(Notification):
  def send(self, message):
    print(f"Sending email notification: {message}")

class SMSNotification(Notification):
  def send(self, message):
    print(f"Sending SMS notification: {message}")

EmailNotification1=EmailNotification()
SMSNotification1=SMSNotification()
EmailNotification1.send("Hello")
SMSNotification1.send("Hello")
