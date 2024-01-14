import random

game_title = "Word Guesser"

word_bank = []

with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

word_to_guess = random.choice(word_bank)

misplaced_letters = []
incorrect_letters = []
max_turns = 5
turns_taken = 0

print("Welcome to ", game_title)
print("The word has 5 letters.")
print("You have ", max_turns, " turns.")

while turns_taken < max_turns:
    guess = input("\nGuess a word:: ").lower()
    if len(guess) != len(word_to_guess):
        print("Please enter a 5-letter word!!")
        continue

    i = 0
    correct_guess = True
    for c in guess:
        if c == word_to_guess[i]:
            print(c, end=" ")
            if c in misplaced_letters:
                misplaced_letters.remove(c)
        elif c in word_to_guess:
            if c not in misplaced_letters:
                misplaced_letters.append(c)
                print("_", end=" ")
                correct_guess = False
        else:
            if c not in incorrect_letters:
                incorrect_letters.append(c)
            print("_", end=" ")
            correct_guess = False
        i += 1

    if correct_guess:
        print("Congratulations, you win!!")
        break

    else:
        print("You have ", max_turns - turns_taken, " turns left.")
        print("\nMisplaced letters: ", misplaced_letters)
        print("Incorrect letters: ", incorrect_letters)
        turns_taken += 1

if turns_taken == max_turns and not correct_guess:
    print("Sorry, you lost. The word was", word_to_guess)
