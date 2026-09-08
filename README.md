# 🎯 Guess the Number Game (Python)

A simple CLI-based number guessing game built with Python. The player has a limited number of attempts to guess a randomly generated number between 1 and 99.

## 🚀 Features

- **Random Number Generation**: Uses Python's `random` module to generate a unique number every game.
- **Limited Attempts**: The player is given a maximum of 5 attempts to guess the correct number.
- **Dynamic Hints**: Provides instant feedback ("Terlalu besar!" or "Terlalu kecil!") after each guess.
- **Clean Code**: Implemented using Python's `for...else` loop construct for clean game flow handling.

## 🛠️ Requirements

- Python 3.x installed on your system.

## 💻 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/guess-the-number.git](https://github.com/YOUR_USERNAME/guess-the-number.git)
   cd guess-the-number

Run the script:

Bash
python main.py
🎮 How to Play
Run the program.

Enter your guess (an integer between 1 and 99).

Read the feedback provided by the terminal.

Try to guess the number within 5 attempts!

📝 Code Overview
Python
import random

random_number = random.randint(1, 99)
max_attempt = 5

for attemp in range(1, max_attempt + 1):
    guess_number = int(input(f"Guess a number from 1 to 99: "))
    
    if guess_number == random_number:
        print(f"Selamat! Tebakan Anda benar yaitu angka {guess_number}")
        break
    elif guess_number > random_number:
        print("Terlalu besar!")
    else:
        print("Terlalu kecil!")
else:
    print(f"Sayang sekali, kesempatan habis! Angka yang benar adalah {random_number}.")
📄 License
This project is open source and available under the MIT License.