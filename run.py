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

for i <= 5:
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(colored(guess[i], 'red'), end="")
        print()

        if guess == word:
            print(colored(f"Woo! Nice Job! You answered right after {attempt} attempts", 'red'))
            break
        elif attempt == 6:
            print(f"Nice try. The answer for this round was {word}")
    play_again = input("Ready for Another Round? Type q and press enter to exit.")
