import random


class GuessTheNumberGame:
    def __init__(self, min_range, max_range, max_attempts):
        # Initialization method to set up the game
        self.secret_number = random.randint(min_range, max_range)  # Generate a random number as the secret number
        self.min_range = min_range  # Minimum range for the secret number
        self.max_range = max_range  # Maximum range for the secret number
        self.max_attempts = max_attempts  # Maximum number of attempts allowed
        self.attempts_left = max_attempts  # Counter for remaining attempts
        self.guess_history = []  # List to store user's guess history

    def get_user_guess(self):
        # Method to get the user's guess from input
        while True:
            try:
                guess = int(input(f"Guess the number between {self.min_range} and {self.max_range}: "))
                return guess
            except ValueError:
                print("Please enter a valid number.")

    def give_hint(self, guess):
        # Method to provide a hint based on the user's guess
        if guess < self.secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

    def play_game(self):
        # Method to execute the main game loop
        print("Welcome to Guess the Number Game!")
        while self.attempts_left > 0:
            user_guess = self.get_user_guess()  # Get the user's guess
            self.guess_history.append(user_guess)  # Add the guess to the history

            if user_guess == self.secret_number:
                print(f"Congratulations! You guessed the number {self.secret_number} correctly.")
                break
            else:
                self.give_hint(user_guess)  # Provide a hint based on the user's guess
                self.attempts_left -= 1  # Decrease the remaining attempts
                print(f"Attempts left: {self.attempts_left}")

        if self.attempts_left == 0:
            print(f"Sorry, you've run out of attempts. The correct number was {self.secret_number}.")

    def show_guess_history(self):
        # Method to display the user's guess history
        print("Guess History:", self.guess_history)


if __name__ == "__main__":
    # Main part of the script
    min_range = 1
    max_range = 100
    max_attempts = 7

    game = GuessTheNumberGame(min_range, max_range, max_attempts)  # Create an instance of the game
    game.play_game()  # Start the game
    game.show_guess_history()  # Display the guess history
