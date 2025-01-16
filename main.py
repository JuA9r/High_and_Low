"""
    High And Low sample.run

This file contain running "High And Low" sample program.
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


class High_and_Low:
    def __init__(self) -> None:
        self.tramp = Tramp()
        self.player = Player()
        self.ai = AI()

    def running(self) -> None:
        print("Game Start")
        current_card = self.tramp.card_draw()

        done = None
        while current_card is not done:
            print(f"Current card: {current_card}")
            guess = input("Next card is High(H) or Low(L)? ").strip().upper()

            if guess == "-1":
                break

            elif guess not in ["H", "L"]:
                print("Please enter 'H' or 'L'\n")
                continue

            next_card = self.tramp.card_draw()
            if next_card is None:
                break

            ai_guess = self.ai.make_judge()
            print(f"AI guessed: {'High' if ai_guess == 'H' else 'Low'}")

            if guess == "H" and next_card > current_card or \
                    guess == "L" and next_card < current_card:
                print("Correct!\n")
                self.player.update_score()

            else:
                print("Incorrect!\n")

            if ai_guess == "H" and next_card > current_card or \
                    ai_guess == "L" and next_card < current_card:
                self.ai.update_score()

            print(f"Card result is: {next_card}")
            print(f"Player score: {self.player.player_score}")
            print(f"AI score: {self.ai.ai_score}")
            print("-"*20)

            current_card = next_card

        print("\nGame Over\n")
        print(
            f"{"-"*20}\nYou Win" if self.player.score > self.ai.score else
            f"{"-"*20}\nYou Lose" if self.player.score < self.ai.score else
            f"{"-"*20}\nDraw"
        )


def main():
    game = High_and_Low()
    game.running()


if __name__ == "__main__":
    main()

