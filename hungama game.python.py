import random

words = ["python", "apple", "banana", "coding", "laptop"]
word = random.choice(words)

guessed = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")

while wrong_guesses < max_guesses:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess! Remaining:", max_guesses - wrong_guesses)

if wrong_guesses == max_guesses:
    print("Game Over! The word was:", word)
    