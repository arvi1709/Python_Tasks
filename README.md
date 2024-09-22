# Python Mini Projects

This repository contains three simple Python projects built using Tkinter and core Python functionalities. Each project showcases basic yet important concepts, such as API requests, GUI creation, and randomness, which are useful for beginners in Python.

## 1. Currency Converter (Tkinter)

### Description
This application allows users to convert an amount from one currency to another using the latest exchange rates. The exchange rates are fetched from an external API.

### Features:
- Input the amount, source currency, and target currency.
- Get the converted value with a simple button click.
- Basic error handling and user-friendly message display.

### Libraries Used:
- `tkinter` for GUI.
- `requests` for fetching exchange rates.
- `messagebox` for displaying error messages.

### Usage:
Run the `currency_converter.py` file. Enter the amount, source currency (e.g., USD), and target currency (e.g., INR). Click 'Convert' to see the conversion result.

---

## 2. Tic Tac Toe (Tkinter)

### Description
This is a two-player Tic Tac Toe game where users can take turns playing. The game tracks the winner or if the game ends in a tie.

### Features:
- Simple 3x3 grid where players can click to mark X or O.
- Detects win or tie conditions and prompts users.
- Resets automatically after a game is finished.

### Libraries Used:
- `tkinter` for GUI.
- `messagebox` for displaying game outcomes.

### Usage:
Run the `tictactoe.py` file. Players take turns clicking on the buttons to mark X or O. The game will display a message when a player wins or if the game ties, followed by resetting the board.

---

## 3. Random Password Generator

### Description
This script generates a random, secure password of a user-defined length. The generated password contains uppercase and lowercase letters, digits, and special characters.

### Features:
- Ensures at least one uppercase letter, one lowercase letter, one number, and one special character.
- Password length validation (minimum length of 4 characters).
- Randomized password with shuffled character positions.

### Libraries Used:
- `random` for generating random characters.
- `string` for accessing character sets.

### Usage:
Run the `password_generator.py` file. Input the desired length of the password (minimum 4). The script will generate and display a secure password.

---

## Requirements
- Python 3.x
- `tkinter` (for GUI-based projects)
- `requests` (for the Currency Converter project)

Install the required libraries using:
```bash
pip install tkinter requests
