# <ins> HANGMAN PROJECT

![Picture of Hangman.](https://cms-assets.tutsplus.com/cdn-cgi/image/width=360/uploads/users/211/posts/23041/final_image/hangmancapture.gif)

## Table of Contents 
1. Description of the Project
2. Installation Instructions
3. Usage Instructions
4. File Structure of the Project
5. License Information

### 1. What is the aim of this Project?

The aim of this project is to develop my skills with python and GitHub by creating an implimentation of the classic game of Hangman. Instead of the game being played between two humans, here the *computer* thinks of a word and the user tries to guess it.

In thie project, I have developed my skills in OOP, creating methods/functions and improved my understanding of GitHub and local repositories.

### 2. Installation Instructions
- **Step 1. Clone the repository to your machine.** 
     - Enter: ```git clone https://github.com/madsjoyce/hangman.git ```into your terminal.
- **Step 2. Navigate to the project directory.**
     - Enter: ```cd Hangman``` into your terminal.

- **Step 3. Run the Hangman game.**
     - Enter: ```python hangman.py``` into your terminal.
- **Step 4. Follow the onscreen instructions to guess the letter and play the game.**
     - ```python 
        # Import play_game from hangman
        from hangman import play_game
        # Play the Hangman game
        play_game(word_list)
- **Step 5. Have fun!** 🤩

### 3. Usage Instructions
You will be given 5 lives in this game, to guess the word that the computer is thinking of. You will need to follow the instructions as the game goes on. 

### 4. File Structure of the Project
The project has been made up of multiple python files named milstone_(x).py which contain the code for specific features of the project.
- **Milestone 1:** was not actually a file, rather this was the stage at which I set up my GitHub repository so that I could save my work remotely.

- **Milestone 2:** contains the code that set up the variables for the game. This included defining the list of possible words, randomising which word the computer chooses to play with, and asking the player to input a single-charactered guess.

- **Milestone 3:** contains the code that checks if the guessed character is in the word. This was done by iteratively checking if the input is a valid guess and then using if and else statements to check if the guessed character was in the word. Lastly, I creating functions that would run these checks, and therefore improve the functionality of my code. 
- **Milestone 4:** the aim here was to use OOP to develop a complete hangman game using a Hangman class. Within this class, I created methods for running the checks needed for the game and defined what happeens if a letter is or is NOT in a word.

- **Milestone 5:** was where the previous Milestone was combined with a new function called play_game, that used the class Hangman to activate the game play.


### 5. License Information
Please click on the link below for license information:

> [Link to License](LICENSE.txt)

