import random
import os 

class Player:
    def __init__(self,):
        self.name = ""
        self.symbol = ""
    
    def choose_name(self):
        while True:
            name=input("Please enter your name:")
            if name.isalpha():
                self.name=name
                break
            print("Invalid name. Please enter a valid name.")
    
    def choose_symbol(self):
        while True:
            symbol=input("Please choose your symbol (X or O):")
            if symbol.upper() in ['X','O']:
                self.symbol=symbol.upper()
                break
            print("Invalid symbol. Please choose either X or O.")
            
            

class Menu:
    
    def display_main_menu(self):
        print("Welcome to Tic Tac Toe")
        print("1. Start Game")
        print("2. Quit Game")
        return input("Please select an option (1 or 2) only: ")
    
    def display_end_game_menu(self):
        print("Thank you for playing Tic Tac Toe!")
        print("1. Restart Game")
        print("2. Quit Game")
        return input("Please select an option (1 or 2) only: ")

class Board:
    def __init__(self):
        self.board=[str(i) for i in range(1,10)]
    
    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i<6:
                print("_"*12)
    
    def update_board(self,position,symbol):
        if 1<=position<=9 and self.board[position-1].isdigit():
            self.board[position-1]=symbol
            return True
        return False
    
    def reset_board(self):
        self.board=[str(i) for i in range(1,10)]
        
class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()

        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for i, player in enumerate(self.players):
            print(f"\nPlayer {i + 1} enter your details:")
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        while True:
            self.play_turn()

            if self.check_win() or self.check_draw():
                self.board.display_board()

                if self.check_draw() and not self.check_win():
                    print("\nIt's a Draw!")

                choice = self.menu.display_end_game_menu()

                if choice == "1":
                    self.reset_game()
                else:
                    self.quit_game()

                break

    def play_turn(self):
        player = self.players[self.current_player_index]

        print(f"\n{player.name}'s turn ({player.symbol})")
        self.board.display_board()

        while True:
            try:
                choice = int(input("Choose a position (1-9): "))

                if 1 <= choice <= 9 and self.board.update_board(choice, player.symbol):
                    break

                print("Invalid move, try again.")

            except ValueError:
                print("Please enter a valid number.")

        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        win_combos = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        for combo in win_combos:
            if (
                self.board.board[combo[0]]
                == self.board.board[combo[1]]
                == self.board.board[combo[2]]
            ):
                winner = self.players[1 - self.current_player_index]
                print(f"\nPlayer {winner.name} wins!")
                return True

        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def reset_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def quit_game(self):
        print("Thank you for playing!")

game=Game()
game.start_game()
