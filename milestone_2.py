import random

def choose_random_word(word_list):
    """Choose a random word from the given list."""
    return random.choice(word_list)

def get_player_guess():
    """Ask the user to input a single letter."""
    return input('Please enter a single letter:')

def is_valid_guess(guess):
    """Check if the input is a valid single letter."""
    return len(guess) == 1 and guess.isalpha()

# My list of fruits:
word_list = ['apple', 'banana', 'cherry', 'peach', 'mango']
print(word_list)

# Create a random word from the list
random_word = choose_random_word(word_list)
print(random_word)

# Ask user to input letter
player_guess = get_player_guess()

# Check if input is valid
if is_valid_guess(player_guess):
    print('Good Guess!')
else:
    print("Oops! That is not a valid input.")
 