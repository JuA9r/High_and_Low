"""
    High And Low.run

This file contain running "High And Low" program.
"""

import random


class Tramp:
    def __init__(self) -> None:
        self.cards = self.gen_cards()

    @staticmethod
    def gen_cards() -> list[int]:
        cards = [i for i in range(1, 14)] * 2
        random.shuffle(cards)
        return cards

    def card_draw(self) -> int:
        return self.cards.pop() if self.cards else None


class Player:
    def __init__(self) -> None:
        self._score = 0

    @property
    def player_score(self) -> int:
        return self._score

    @player_score.setter
    def player_score(self, value: int) -> None:
        self._score = value

    def update_score(self) -> None:
        self._score += 1

    def __add__(self, other):
        return self._score + other._score if isinstance(other, Player) else other

    def __str__(self) -> str:
        return f"Player score: {self._score}"


class AI:
    def __init__(self) -> None:
        self._score = 0

    @property
    def ai_score(self) -> None:
        return self._score

    @ai_score.setter
    def ai_score(self, value: int) -> None:
        self._score = value

    def update_score(self) -> None:
        self._score += 1

    @staticmethod
    def make_judge() -> str:
        return random.choice(["H", "L"])

    def __add__(self, other):
        return self._score + other._score if isinstance(other, AI) else other

    def __str__(self) -> str:
        return f"AI score: {self._score}"


class High_and_Low:
    def __init__(self) -> None:
        self.__tramp = Tramp()
        self.__player = Player()
        self.__ai = AI()

    def running(self) -> None:
        print("Game Start")
        current_card = self.__tramp.card_draw()

        done = None
        while current_card is not done:
            print(f"Current card: {current_card}")
            guess = input("Next card is High(H) or Low(L)? ").strip().upper()

            if guess == "-1":
                break

            elif guess not in ["H", "L"]:
                print("Please enter 'H' or 'L'\n")
                continue

            next_card = self.__tramp.card_draw()
            if next_card is None:
                break

            ai_guess = self.__ai.make_judge()
            print(f"AI guessed: {'High' if ai_guess == 'H' else 'Low'}")

            if guess == "H" and next_card > current_card or \
                    guess == "L" and next_card < current_card:
                print("Correct!\n")
                self.__player.update_score()

            else:
                print("Incorrect!\n")

            if ai_guess == "H" and next_card > current_card or \
                    ai_guess == "L" and next_card < current_card:
                self.__ai.update_score()

            print(f"Card result is: {next_card}")
            print(self.__player.__str__())
            print(self.__ai.__str__())
            print("-"*20)

            current_card = next_card

        print("\nGame Over\n")

        print(
            f"{"-"*20}\nYou Win" if self.__player.score > self.__ai.score else
            f"{"-"*20}\nYou Lose" if self.__player.score < self.__ai.score else
            f"{"-"*20}\nDraw"
        )


def main():
    game = High_and_Low()
    game.running()


if __name__ == "__main__":
    main()