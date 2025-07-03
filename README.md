# ❄️ Snowman Meltdown - A Word Guessing Game

![Game Preview]

## 📖 Overview
A Python implementation of the classic word-guessing game with a winter twist! Guess letters to reveal the hidden word before your snowman completely melts.

## ✨ Features
- **Gradual melting animation** with 8 distinct stages
- **Custom ASCII art** snowman that melts piece by piece
- **Smart input validation** for:
  - Single letters only
  - No duplicate guesses
  - Alphabet characters only
- **Play again** option without restarting
- **Clear visual feedback** showing:
  - Current word progress
  - Guessed letters
  - Mistakes remaining

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/snowman-meltdown.git
2. Navigate to project directory:
    ```bash
    cd snowman-meltdown
    ```
🎮 How to Play

Run the game:
```bash
python snowman.py
```
Gameplay:

1. Guess one letter at a time

2. Correct guesses reveal letters in the word

3. Wrong guesses melt the snowman

4. Win by guessing the word before complete meltdown!

🏗️ Project Structure:
```bash
Snowman-Meltdown/
├── snowman.py        # Main game executable
├── game_logic.py     # Core game functions
├── ascii_art.py      # Snowman melting stages
└── README.md         # This file
```
📜 License
MIT License - see LICENSE file for details