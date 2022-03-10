# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from termcolor import colored

def game_word():
    with open("word_bank.txt") as f:
        chosen_word = f.read().splitlines()
        return random.choice(chosen_word)


print("Let's play Wordle:")
print("Type a 5 letter word and hit enter!\n")
play_again = ""
while play_again != "q":
    
    word = game_word().lower()
    for attempt in range(1, 7):
        guess = input().lower()
        try:
            if len(guess) != 5:
                raise ValueError(
                    f"Word must be 5 letters long, your word had {len(guess)}"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
             



        for i in range( 0, 5):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            print(colored(f"Woo! You answered in {attempt} attempts", 'red'))
            break
        elif attempt == 6:
            print(f"Nice try. The answer for this round was {word}")
    play_again = input("Let's Go Again? Type q and press enter to exit.")
