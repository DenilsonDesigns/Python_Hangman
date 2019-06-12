# importing the time module
import time

# welcoming the user
name = input("What is your name? ")

print("Hello, "+name, "Time to play hangman!")
print()

# wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# here we set the secret
word = "secret"

# creates a variable with an empty value
guesses = ''

# determine the number of max turns
turns = 10

# Create a while loop

# check if the turns are more than zero
while turns > 0:

    # make a counter that starts with zero
    failed = 0

    # for every character in word to guess
    word_to_print = ''
    for char in word:
        # see if the char is in the players guess
        if char in guesses:
            # print out the characters
            word_to_print += char+" "
        else:
            # if not found, print a dash
            word_to_print += "_ "
            failed += 1

    print(word_to_print)
    if failed == 0:
        print("You won!")
        # exit the script
        break

    print()
    # ask the user to guess a character
    guess = input("Guess a character: ")
    # set the players guess to guesses
    guesses += guess
    # if the guess is not found in the secret word:
    if guess not in word:
        # turns counter decreases
        turns -= 1
        # Print wrong
        print("This character is not in the word")
        # Print amount of turns left
        print("You have ", +turns, "more guesses")
        # if the turns are equal to zero
        if turns == 0:
            print("You lose :(")
