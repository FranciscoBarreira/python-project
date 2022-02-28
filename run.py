# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random


def game_word():
    with open("word_bank.txt") as f:
        chosen_word = f.read().splitlines()
        return random.choice(chosen_word)

print("Let's play Wordle:")
print("Type a 5 letter word and hit enter!\n")
