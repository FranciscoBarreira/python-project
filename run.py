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

word = game_word().lower()
for attempt in range(1, 7):
    guess = input().lower()
    try:
        if len(guess) != 5:
            raise ValueError(
                f"The word must be 5 letters long, your word was {len(guess)} letters long"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

    if guess == word:
        print(colored(f"Woo! Nice Job! You answered right after {attempt} attempts", 'red'))
        break
    elif attempt == 6:
        print(f"Nice try. The answer was {word}")
