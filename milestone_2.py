import random #imports random function

# My list of fruits:
word_list = ['apple', 'banana', 'cherry', 'peach', 'mango']
print(word_list)

#Create a random word from the list
word = random.choice(word_list)
print(word)

# Ask user to input letter
guess = input('Please enter a single letter:')

#check input is valid
if len(guess) == 1 and guess.isalpha():
  print('Good Guess!')

else:
 print("Oops! That is not a valid input.")

 