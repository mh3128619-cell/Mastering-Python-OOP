class User:
    def __init__(self, name, gender, is_subscribed):
        self.name = name
        self.gender = gender
        self.is_subscribed = is_subscribed
    
    def get_title(self):
        if self.gender == "male":
            return "Mr."
        elif self.gender == "female":
            return "Ms."
        else:
            return ""
    
    def welcome_message(self):
        title = self.get_title()
        if self.is_subscribed:
            print(f"Welcome {title} {self.name}! You are a premium subscriber.")
        else:
            print(f"Welcome {title} {self.name}! Please subscribe to get more features.")

user1 = User("Ahmed", "male", True)
user2 = User("Mona", "female", False)

user1.welcome_message()
user2.welcome_message()
