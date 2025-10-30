"""
    High_and_Low.run

This file contains running High_and_Low program.
"""

"""import module"""

import random
import textwrap
from collections import defaultdict
from typing import Optional, Iterator


class Tramp:
    def __init__(self) -> None:
        self.__cards = self.gen_cards()

    @staticmethod
    def gen_cards() -> list[int]:
        """Generate a shuffled deck of cards"""
        cards = [i for i in range(1, 14)] * 4
        random.shuffle(cards)
        return cards

    def card_draw(self) -> Optional[int]:
        """Draw a card from the deck"""
        return self.__cards.pop() if self.__cards else None

    """for debugging"""

    def __len__(self) -> int:
        return len(self.__cards)

    def __contains__(self, card: int) -> bool:
        return card in self.__cards

    def __getitem__(self, index: int) -> int:
        return self.__cards[index]

    def __setitem__(self, key, value: any) -> None:
        self.__cards[index] = value

    def __delitem__(self, key: int) -> None:
        del self.__cards[key]

    def __iter__(self) -> Iterator[int]:
        return iter(self.__cards)

    def __reversed__(self) -> Iterator[int]:
        return reversed(self.__cards)

    def __str__(self):
        return f"Deck of\n{textwrap.fill(', '.join(map(str, self.__cards)), 44)}\n"


class Player:
    def __init__(self, name: str = input("your name: ")) -> None:
        self._score = 0
        self.__name = name

    def update_score(self) -> None:
        self._score += 1

    def __call__(self) -> int:
        return self._score

    def __repr__(self) -> str:
        return f"{self.__name} score: {self._score}"


class AI(Player):
    @staticmethod
    def make_judge() -> str:
        return random.choice(["H", "L"])


class HighAndLow:
    def __init__(self) -> None:
        self.__tramp = Tramp()
        self.__player = Player()
        self.__ai = AI(name="AI")

    def determine_winner(self) -> str:
        return "You Win!" if self.__player() >= self.__ai() else \
            "You Lose!" if self.__player() <= self.__ai() else \
            "It's a Draw!"

    def running(self) -> None:
        print("Game Start!")
        current_card = self.__tramp.card_draw()

        while current_card is not None:
            print(f"\nCurrent card: {current_card}")
            guess = input("Next card is High (H) or Low (L)? ('-1' to quit): ").strip().upper()

            if guess == "-1":
                print("\nGame aborted.")
                break

            if guess not in ["H", "L"]:
                print("Invalid input. Please enter 'H' or 'L'.")
                continue

            next_card = self.__tramp.card_draw()
            if next_card is None:
                print("No more cards left!")
                break

            ai_guess = self.__ai.make_judge()
            print(f"AI guessed: {'High' if ai_guess == 'H' else 'Low'}")

            # Determine results for both player and AI
            if guess == "H" and next_card >= current_card or \
                    guess == "L" and next_card <= current_card:
                print("\nYou guessed correctly!")
                self.__player.update_score()
            else:
                print("\nYou guessed wrong!")

            if ai_guess == "H" and next_card >= current_card or \
                    ai_guess == "L" and next_card <= current_card:
                self.__ai.update_score()

            print(f"\n{"-" * 20}\nNext card was: {next_card}")
            print(self.__player)
            print(self.__ai)
            print("-" * 20)

            current_card = next_card

        print("\nGame Over!")
        print(self.__player.__repr__()+"\n"+self.__ai.__repr__())
        print(self.determine_winner())


def main():
    game = HighAndLow()
    game.running()


if __name__ == "__main__":
    main()
