# 🎯 Guess the Number Game

A simple command-line number guessing game built with **Python**. The player must guess a randomly generated number between **1 and 99** within a maximum of **5 attempts**.

## 🚀 Features

* 🎲 **Random Number Generation**
  Generates a random number between 1 and 99 using Python's built-in `random` module.

* 🎯 **Limited Attempts**
  Players have a maximum of 5 attempts to guess the correct number.

* 💡 **Dynamic Hints**
  Provides feedback after every incorrect guess:

  * `Terlalu besar!`
  * `Terlalu kecil!`

* 🧹 **Clean Game Flow**
  Uses Python's `for...else` loop to handle the game logic when the player either guesses correctly or runs out of attempts.

## 🛠️ Requirements

Before running the project, make sure you have:

* **Python 3.x**
* A terminal or command prompt

You can check your Python version with:

```bash
python --version
```

## 💻 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/guess-the-number.git
```

### 2. Navigate to the Project Directory

```bash
cd guess-the-number
```

### 3. Run the Program

```bash
python main.py
```

## 🎮 How to Play

1. Run the program using the command above.
2. Enter an integer between **1 and 99**.
3. The program will tell you whether your guess is:

   * Too high (`Terlalu besar!`)
   * Too low (`Terlalu kecil!`)
4. Continue guessing until you find the correct number.
5. You have a maximum of **5 attempts**.
6. If you fail to guess the number, the program will reveal the correct answer.

### Example

```text
Guess a number from 1 to 99: 50
Terlalu besar!

Guess a number from 1 to 99: 25
Terlalu kecil!

Guess a number from 1 to 99: 37
Selamat! Tebakan Anda benar yaitu angka 37
```

## 📝 Code Overview

The game uses Python's `random.randint()` to generate the target number and a `for...else` loop to manage the limited attempts.

```python
import random

random_number = random.randint(1, 99)
max_attempt = 5

for attempt in range(1, max_attempt + 1):
    guess_number = int(input("Guess a number from 1 to 99: "))

    if guess_number == random_number:
        print(f"Selamat! Tebakan Anda benar yaitu angka {guess_number}")
        break
    elif guess_number > random_number:
        print("Terlalu besar!")
    else:
        print("Terlalu kecil!")
else:
    print(
        f"Sayang sekali, kesempatan habis! "
        f"Angka yang benar adalah {random_number}."
    )
```

## 📂 Project Structure

```text
guess-the-number/
│
├── main.py
└── README.md
```

## 📚 Concepts Practiced

This project is useful for practicing several Python fundamentals:

* Variables
* `random` module
* `random.randint()`
* User input with `input()`
* Type conversion with `int()`
* Conditional statements (`if`, `elif`, `else`)
* `for` loops
* `for...else`
* `break`
* String formatting with f-strings

## 🔮 Possible Improvements

Some ideas for future improvements:

* [ ] Add input validation for non-integer input.
* [ ] Prevent guesses outside the range of 1–99.
* [ ] Add difficulty levels with different attempt limits.
* [ ] Add a score system.
* [ ] Allow the player to play multiple rounds.
* [ ] Add a replay option after each game.
* [ ] Track the player's best score.

## 📄 License

This project is open source and available under the **MIT License**.

See the `LICENSE` file for more information.
