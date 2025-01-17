import random
from typing import Iterator, Optional


class Tramp:
    def __init__(self) -> None:
        self.cards = self.gen_cards()

    @staticmethod
    def gen_cards() -> list[int]:
        """Generate a shuffled deck of cards"""
        cards = [i for i in range(1, 14)] * 2
        random.shuffle(cards)
        return cards

    def card_draw(self) -> Optional[int]:
        """Draw a card from the deck"""
        return self.cards.pop() if self.cards else None

    """for debugging"""

    def __len__(self) -> int:
        return len(self.cards)

    def __contains__(self, card: int) -> bool:
        return card in self.cards

    def __getitem__(self, index: int) -> int:
        return self.cards[index]

    def __iter__(self) -> Iterator[int]:
        return iter(self.cards)


class Player:
    def __init__(self, name: str = "Player") -> None:
        self._score = 0
        self.name = name

    def update_score(self) -> None:
        self._score += 1

    def __call__(self) -> int:
        return self._score

    def __repr__(self) -> str:
        return f"{self.name} score: {self._score}"


class AI(Player):
    @staticmethod
    def make_judge() -> str:
        """AI makes a guess: High (H) or Low (L)"""
        return random.choice(["H", "L"])


class HighAndLow:
    def __init__(self) -> None:
        self.__tramp = Tramp()
        self.__player = Player()
        self.__ai = AI(name="AI")

    def determine_winner(self) -> str:
        """Determine the game winner"""
        return "You Win!" if self.__player() > self.__ai() else \
            "You Lose!" if self.__player() < self.__ai() else \
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
            if (guess == "H" and next_card > current_card) or \
               (guess == "L" and next_card < current_card):
                print("\nYou guessed correctly!")
                self.__player.update_score()
            else:
                print("\nYou guessed wrong!")

            if (ai_guess == "H" and next_card > current_card) or \
               (ai_guess == "L" and next_card < current_card):
                self.__ai.update_score()

            print(f"\n{"-"*20}\nNext card was: {next_card}")
            print(self.__player)
            print(self.__ai)
            print("-" * 20)

            current_card = next_card

        print("\nGame Over!")
        print(self.determine_winner())


def main():
    game = HighAndLow()
    game.running()


if __name__ == "__main__":
    main()
