# 68
# 69
# 70
# 71
# 72
# 73
# Step 1
# TODO-1 Randomnly choose a word from the word_list and assign it to a variables called chosen_word.
# For each letter in the chosen_word, add a "_" to 'display'
# So if the chosen_word was "apple", display should be ["_","_","_","_","_"] with 5 "_" representiong each letter to guess.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowecase/
# if the letter at that position matches "guess" then reveal that letter in the display at that position.
# e.g. IF the user guessed "p"and the chosen word was "apple", then display should be ["_", "p","p","_","_"].
# TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
# Print "display" and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - dont worry about getting the user to guess the next letter. We'll tackle that in step 3
from reprlib import clear
import random
import hangman_words
from hangman_words import word_list
from hangman_art import logo, stages

# word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# 76
end_of_game = False
lives = 6
# 75

print(logo)
# Step 2
# Testing code
print(f'Pssst, the solution is {chosen_word}. ')


# Create blacks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

        # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        # else:
        #     print("No match")
    # if letter == guess:
    #     print("Right")
    # else:
    #     print("Wrong")

    if guess not in chosen_word:
        print(
            f"You've guessed {guess}, that's not in the word. Tou lose life. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You WIN")
    print(stages[lives])

# 77
# 78
