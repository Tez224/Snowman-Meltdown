import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """
    Starts the game loop: prompt user to guess a letter,
    shows selected letter.
    Checks if input is valid and correct.

    Displays win or loose the game massage in the end
    and asks if player wants to play again.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while mistakes < len(ascii_art.STAGES) :
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if len(guess) > 1:
            guess = input("please guess a single letter! Try again: ")

        if guess in guessed_letters:
            print("correct guess!")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Win! You guessed the word: {secret_word}!")

            play_again = input("Would you like to play again? (Y/N): ")

            if play_again.lower() == "y":
                play_game()
            if play_again.lower() == "n":
                break
            else:
                print("Invalid input: Y/N were possible. Game Ends.")
                break



        if mistakes == len(ascii_art.STAGES) - 1:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Game Over! The word was {secret_word}.")

            play_again = input("Would you like to play again? (Y/N): ")

            if play_again.lower() == "y":
                play_game()
            if play_again.lower() == "n":
                break
            else:
                print("Invalid input: Y/N were possible. Game Ends.")
                break


def display_game_state(mistakes, secret_word, guessed_letters):
    """
     Displays _ for every letter in secret word.
     Displays actual number of guessed letters and mistakes
     Adds the correct letter on the correct place in the secret word.

    :param mistakes: increase mistake += 1 by mistake
    :param secret_word: str: secret word
    :param guessed_letters: list of guessed letters
    """
    print(ascii_art.STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"Word: {display_word}\n")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Mistakes: {mistakes}\n\n")


if __name__ == "__main__":
    play_game()