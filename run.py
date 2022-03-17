# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from termcolor import colored

MAX_ATTEMPTS = 6

def get_random_word():
    with open("word_bank.txt") as f:
        chosen_word = f.read().splitlines()
        return random.choice(chosen_word)


def show_instructions():
    print("Type any 5 letter word to start playing the game.")
    print("A random word will be chosen from the word_bank file")
    print("The word you typed will appear with differently colored letters.")
    print("If the letter is in the original word, but in the wrong place,")
    print("it will be coloured yellow.")
    print("If the letter is in the original word, and in the right place,")
    print("it will be coloured green.")
    print("You have 6 attempts to figure out the original word")


def show_menu():
    while True:
        select_option = input("Type 1) Play game, 2) Instructions 3) Quit\n")
        if select_option == '1':
            start_game()
            break
        elif select_option == '2':
            show_instructions()
            break
        elif select_option == '3':
            print('Thanks for playing')
            break
        else: 
            try:
                if select_option != 1 and 2 and 3:
                    raise ValueError(
                        f"Please type 1, 2 or 3. You typed {select_option}"
                    )
                else:
                    return select_option
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
   

def take_user_guess():
    while True:
        guess = input("Type any 5 letter word and press enter!\n").lower()
        try:
            if len(guess) != 5:
                raise ValueError(
                    f"Word must be 5 letters long, your word had {len(guess)}"
                )
            else:
                return guess
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

def start_game():
    is_game_running = True
    while is_game_running:
        word = get_random_word().lower()
        for attempt in range(1, MAX_ATTEMPTS + 1):
            user_guess = take_user_guess()
            for i in range(0, 5):    # Since word is a 5 letter word
                if user_guess[i] == word[i]:     # If position of letter matches in original word
                    print(colored(user_guess[i], 'green'), end="")
                elif user_guess[i] in word:     # If letter is present in original word
                    print(colored(user_guess[i], 'yellow'), end="")
                else:
                    print(user_guess[i], end="")
            print("\n")

            if user_guess == word:
                print(colored(f"Woo! You got it in {attempt} attempts", 'red'))
                break
            elif attempt == 6:
                print(f"Nice try. The answer for this round was {word}")
        play_again = input("Let's Go Again? Type q and press enter to exit.")
        if play_again == 'q':
            is_game_running = False
       

def print_welcome_msg():
    print("It's time for Wordle:")

def main():
    print_welcome_msg()
    show_menu()


main()