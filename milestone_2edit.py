import random #imports random function

# My list of fruits:
word_list = ['apple', 'banana', 'cherry', 'peach', 'mango']
print(word_list)

#Create a random word from the list
random_word = random.choice(word_list)
print(random_word)

# Ask user to input letter
player_guess = input('Please enter a single letter:')

#check input is valid
if len(player_guess) == 1 and guess.isalpha():
  print('Good Guess!')

else:
 print("Oops! That is not a valid input.")