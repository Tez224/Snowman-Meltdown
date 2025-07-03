from game_logic import play_game

def main():
    print("=== Snowman Meltdown Game ===")
    while True:
        if not play_game():
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
