from abc import ABCMeta, abstractmethod

class PaymentProcessor(metaclass=ABCMeta):
  @abstractmethod
  def process_payment(self):
    pass

class CreditCardPayment(PaymentProcessor):
  def process_payment(self):
    print("Processing credit card payment")

class PayPalPayment(PaymentProcessor):
  def process_payment(self):
    print("Processing PayPal payment")


pay1=CreditCardPayment()
pay2=PayPalPayment()
pay1.process_payment()
pay2.process_payment()
