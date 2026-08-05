import random


class Player:
    def __init__(self, is_computer=False):
        self.name = ""
        self.symbol = ""
        self.is_computer = is_computer

    def choose_name(self):
        while True:
            name = input("Enter your name: ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use letters only.")

    def choose_symbol(self, taken_symbol=None):
        while True:
            symbol = input(f"{self.name}, choose your symbol (single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                symbol = symbol.upper()
                if taken_symbol and symbol == taken_symbol:
                    print("This symbol is already taken. Choose another one.")
                    continue
                self.symbol = symbol
                break
            print("Invalid symbol. Please choose a single letter.")


class Menu:
    def display_main_menu(self):
        print("\n--- Welcome to Tic Tac Toe ---")
        print("1. Start Game")
        print("2. Quit Game")
        return input("Enter your choice (1 or 2): ")

    def display_mode_menu(self):
        print("\n--- Choose Game Mode ---")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        return input("Enter your choice (1 or 2): ")

    def display_end_game_menu(self):
        print("\n--- Game Over ---")
        print("1. Restart Game")
        print("2. Quit Game")
        return input("Enter your choice (1 or 2): ")


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i + 3]))
            if i < 6:
                print("---------")

    def update_board(self, position, symbol):
        if self.board[position - 1].isdigit():
            self.board[position - 1] = symbol
            return True
        return False

    def available_positions(self):
        return [i + 1 for i, cell in enumerate(self.board) if cell.isdigit()]

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    WIN_COMBOS = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

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
            # The user quit before playing anything, so no "thanks for playing"
            self.quit_game(played=False)

    def setup_players(self):
        mode_choice = self.menu.display_mode_menu()
        vs_computer = mode_choice == "2"

        print("\nPlayer 1 enter your details:")
        self.players[0] = Player()
        self.players[0].choose_name()
        self.players[0].choose_symbol()

        if vs_computer:
            computer = Player(is_computer=True)
            computer.name = "Computer"
            # Pick a symbol different from player 1's
            computer.symbol = "O" if self.players[0].symbol != "O" else "X"
            print(f"\nComputer will play as '{computer.symbol}'.")
            self.players[1] = computer
        else:
            print("\nPlayer 2 enter your details:")
            self.players[1] = Player()
            self.players[1].choose_name()
            self.players[1].choose_symbol(taken_symbol=self.players[0].symbol)

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
                    self.quit_game(played=True)

                break

    def play_turn(self):
        player = self.players[self.current_player_index]

        print(f"\n{player.name}'s turn ({player.symbol})")
        self.board.display_board()

        if player.is_computer:
            choice = self.choose_computer_move(player)
            print(f"Computer chooses position {choice}.")
            self.board.update_board(choice, player.symbol)
        else:
            while True:
                try:
                    choice = int(input("Choose a position (1-9): "))

                    if 1 <= choice <= 9 and self.board.update_board(choice, player.symbol):
                        break

                    print("Invalid move, try again.")

                except ValueError:
                    print("Please enter a valid number.")

        self.current_player_index = 1 - self.current_player_index

    def choose_computer_move(self, computer_player):
        opponent = self.players[1 - self.current_player_index]
        board_cells = self.board.board

        # 1. Try to win
        move = self._find_winning_move(computer_player.symbol)
        if move:
            return move

        # 2. Try to block opponent's win
        move = self._find_winning_move(opponent.symbol)
        if move:
            return move

        # 3. Take the center if free
        if board_cells[4].isdigit():
            return 5

        # 4. Take a random free corner
        corners = [1, 3, 7, 9]
        free_corners = [c for c in corners if board_cells[c - 1].isdigit()]
        if free_corners:
            return random.choice(free_corners)

        # 5. Otherwise take any free cell
        return random.choice(self.board.available_positions())

    def _find_winning_move(self, symbol):
        board_cells = self.board.board
        for combo in self.WIN_COMBOS:
            values = [board_cells[i] for i in combo]
            if values.count(symbol) == 2:
                for i in combo:
                    if board_cells[i].isdigit():
                        return i + 1
        return None

    def check_win(self):
        for combo in self.WIN_COMBOS:
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

    def quit_game(self, played=True):
        if played:
            print("Thank you for playing!")
        else:
            print("See you next time!")


game = Game()
game.start_game()
