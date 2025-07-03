import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def get_valid_guess(guessed_letters):
    """
    Prompts user for a valid single letter guess.
    Repeats until valid input is received.
    """
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter exactly one letter!")
            continue

        if not guess.isalpha():
            print("Please enter a valid letter (a-z)!")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter!")
            continue

        return guess


def play_game():
    """
    Main game loop handling gameplay, win/loss conditions,
    and returns whether player wants to play again.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("\nWelcome to Snowman Meltdown!")
    print("Guess the word before the snowman melts completely!\n")

    while mistakes < len(ascii_art.STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)
        print(f"You guessed: {guess}")

        if guess not in secret_word:
            mistakes += 1
            print(f"Oops! '{guess}' is not in the word. The snowman melts a bit...")

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Congratulations! You saved the snowman! The word was: {secret_word}")
            break

    else:  # This runs if while loop completes without breaking (snowman melted)
        display_game_state(mistakes, secret_word, guessed_letters)
        print(f"Oh no! The snowman melted completely! The word was: {secret_word}")

    while True:
        play_again = input("\nWould you like to play again? (Y/N): ").lower()
        if play_again in ('y', 'n'):
            return play_again == 'y'
        print("Please enter Y or N.")


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
    Displays game progress including snowman art,
    word with blanks/guessed letters, and game info.
    """
    print(ascii_art.STAGES[mistakes])

    display_word = " ".join(letter if letter in guessed_letters else "_"
                            for letter in secret_word)
    print(f"Word: {display_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Mistakes: {mistakes} of {len(ascii_art.STAGES) - 1}\n")
