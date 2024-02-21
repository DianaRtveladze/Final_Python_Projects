import random
from words import word_list


class Hangman:
    def __init__(self):
        self.word = None

    def play(self):
        self._get_word()
        self._game_logic()
        while input("Play Again? (Y/N) ").upper() == "Y":
            self._get_word()
            self._game_logic()

    def _game_logic(self):
        word_completion = "_" * len(self.word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print("Let's play Hangman!")
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            guess = input("Please guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in self.word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(self.word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(self.word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)
                elif guess != self.word:
                    print(guess, "is not the word.")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = self.word
            else:
                print("Not a valid guess.")
            print(word_completion)
            print("\n")
        if guessed:
            print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry, you ran out of tries. The word was " + self.word + ". Maybe next time!")

    def _get_word(self):
        self.word = random.choice(word_list).upper()


if __name__ == "__main__":
    hangman_game = Hangman()
    hangman_game.play()
