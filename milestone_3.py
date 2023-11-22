def check_guess(guess):
    """Check if the guessed letter is in the word."""
    # Step 2: Convert the guess into lowercase
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in random_word:
        print(f'Good guess! {guess} is in the word.')
        return True
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
        return False

def ask_for_input():
    """Ask the user to guess a letter."""
    while True:
        # Step 2: Move the code for asking the user to guess a letter
        guess = input('Guess a letter: ')

        # Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call the check_guess function to check if the guess is in the word
            if check_guess(guess):
                break
        else:
            # If the guess does not pass the checks, print an error message
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Call the ask_for_input function to test the code
ask_for_input()