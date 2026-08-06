class Seat:
    def __init__(self, number, is_booked=False):
        self.number = number
        self.is_booked = is_booked

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"Seat {self.number} has been successfully booked.")
            return True
        else:
            print(f"Seat {self.number} is already booked!")
            return False

    def cancel(self):
        if self.is_booked:
            self.is_booked = False
            print(f"Booking for seat {self.number} has been cancelled.")
            return True
        else:
            print(f"Seat {self.number} is already available (not booked).")
            return False


class Movie:
    def __init__(self, title, duration, price):
        self.title = title
        self.duration = duration
        self.price = price
        self.seats = [Seat(i) for i in range(1, 6)]

    def show_available_seats(self):
        print(f"\n--- Available Seats for {self.title} ---")
        for seat in self.seats:
            status = "Available" if not seat.is_booked else "Booked"
            print(f"Seat {seat.number}: {status}")


class Payment:
    def __init__(self, payment_type):
        self.payment_type = payment_type

    def process_payment(self, amount):
        print("\n--- Processing Payment ---")
        if self.payment_type.lower() == "cash" or self.payment_type == "1":
            print(f"Paid {amount} EGP successfully using Cash.")
            return True
        elif self.payment_type.lower() == "visa" or self.payment_type == "2":
            print(f"Paid {amount} EGP successfully using Visa.")
            return True
        else:
            print("Invalid payment method!")
            return False


class Cinema:
    def __init__(self):
        self.movies = [
            Movie("Batman Movie", "2h 30m", 100),
            Movie("Spiderman Movie", "2h 10m", 120)
        ]

    def show_movies(self):
        print("\nWe have 2 Movies:")
        for idx, movie in enumerate(self.movies, start=1):
            print(f"{idx}. {movie.title} ({movie.duration}) - Price: {movie.price} EGP")


class Customer:
    def __init__(self, name):
        self.name = name
        self.chosen_movie = None

    def choose_movie(self, cinema_obj):
        while True:
            cinema_obj.show_movies()
            choice = input("Please enter what you want (Batman Movie or Spiderman Movie, or 1/2): ").strip()

            if choice.lower() == "batman movie" or choice == "1":
                self.chosen_movie = cinema_obj.movies[0]
                print(f"You selected: {self.chosen_movie.title}")
                break
            elif choice.lower() == "spiderman movie" or choice == "2":
                self.chosen_movie = cinema_obj.movies[1]
                print(f"You selected: {self.chosen_movie.title}")
                break
            else:
                print("Invalid choice, please try again.\n")

    def choose_seat(self):
        if not self.chosen_movie:
            print("Please choose a movie first!")
            return False

        while True:
            self.chosen_movie.show_available_seats()

            try:
                seat_num = int(input("Enter the seat number you want to book: "))

                selected_seat = None
                for seat in self.chosen_movie.seats:
                    if seat.number == seat_num:
                        selected_seat = seat
                        break

                if selected_seat:
                    if selected_seat.book():
                        return True
                else:
                    print("Invalid seat number, please try again.")

            except ValueError:
                print("Please enter a valid number.")

    def pay_for_ticket(self):
        if not self.chosen_movie:
            print("You haven't chosen a movie yet!")
            return

        while True:
            print("\nHow would you like to pay?")
            print("1. Cash")
            print("2. Visa")

            choice = input("Enter your choice (1 or 2): ").strip()

            if choice in ["1", "2", "cash", "visa"]:
                payment_process = Payment(choice)
                success = payment_process.process_payment(self.chosen_movie.price)

                if success:
                    print("Booking completed successfully! Enjoy your movie.")
                    break
            else:
                print("Invalid choice, please choose Cash or Visa.")


class Menu:
    def display_main_menu(self):
        print("\n--- Main Menu ---")
        print("1. Show Movies")
        print("2. Choose Movie & Book Seat")
        print("3. Exit")


if __name__ == "__main__":
    print("Welcome to Cinema System!")
    name = input("Please enter your name: ").strip()

    customer = Customer(name)
    cinema = Cinema()
    menu = Menu()

    while True:
        menu.display_main_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            cinema.show_movies()

        elif choice == "2":
            customer.choose_movie(cinema)
            if customer.choose_seat():
                customer.pay_for_ticket()

        elif choice == "3":
            print("Thank you for visiting! Goodbye")
            break

        else:
            print("Invalid choice, please try again.")
