# **High and Low game**

- This project imprements High and Low using Python.
- This game has a simple rule of thinking about how high or low the next number is.

## **Execution Environment**
- **Python**: 3.13

---

## Table of Contents

- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
- [This Game Rules](#this-game-rules)
- [Licence](#licence)

## How to Run
1. Ensure you have Python installed on your system.
2. Library usage is only for random module
3. Run the program:
   ```bash
   python main.py
   ```

## Features
- **Operability**: Only 2 keys to use
- **operability**: Runs on terminal

### Parameters
- **Tramp.gen_cards()**: Two numbers from 1 to 13 are generated.
- **_score**: Initial value 0 and add 1 point by update_score() for each correct answer

## How to Play
1. **Start**: Launch the game, the numbers of the matching cards will be displayed.
2. **Input text**: Input text is H(High) or L(Low).
3. **Finish game**: Draw all cards or enter -1.

### This game Rules
1. Enter either H or L
2. If the current card and the next card are the same, add 1 to the score
3. The one with the highest score wins

## Licence
This project is licensed under the MIT Licence. See the `LICENCE` file for details.
