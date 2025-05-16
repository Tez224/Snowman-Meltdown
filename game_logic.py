import random
import ascii_art


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    while mistakes < len(ascii_art.STAGES) :
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess in guessed_letters:
            print("correct guess!")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Win! You guessed the word: {secret_word}")
            break

    if mistakes == len(ascii_art.STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)
        print(f"Game Over! The word was {secret_word}")


def display_game_state(mistakes, secret_word, guessed_letters):
    print(ascii_art.STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"Word: {display_word}\n")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Mistakes: {mistakes}")


if __name__ == "__main__":
    play_game()