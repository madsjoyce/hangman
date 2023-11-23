import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.pick_new_word()

    def pick_new_word(self):
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def display_word_guessed(self):
        print("Word guessed so far:", ' '.join(self.word_guessed))

    def update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess

        self.num_letters -= 1

    def handle_correct_guess(self, guess):
        print(f'Good guess! {guess} is in the word.')
        self.update_word_guessed(guess)

    def handle_incorrect_guess(self, guess):
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            self.handle_correct_guess(guess)
        else:
            self.handle_incorrect_guess(guess)

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter: ')

            # Check that the guess is a single alphabetical character
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                self.display_word_guessed()
                break

def play_game(word_list): 
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()

        else:
            print('Congratulations, you won the game!')
            break


play_game(word_list)