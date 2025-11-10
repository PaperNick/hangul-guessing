import random
from typing import List, Optional, Tuple

from src.models import Hangul


class Game:
    def __init__(self, hangul_chars: List[Hangul]) -> None:
        self._correct_guesses = 0
        self._incorrect_guesses = 0
        self._hangul_chars = hangul_chars
        self._current_hangul: Optional[Hangul] = None

    def increment_correct(self) -> int:
        self._correct_guesses += 1
        return self._correct_guesses

    def increment_incorrect(self) -> int:
        self._incorrect_guesses += 1
        return self._incorrect_guesses

    def make_guess(self, roman_guess: str) -> bool:
        if self._current_hangul is None:
            raise ValueError("No hangul character selected. Please generate one first.")

        return roman_guess in self._current_hangul.roman_chars

    def correct_answer(self) -> List[str]:
        if self._current_hangul is None:
            raise ValueError("No hangul character selected. Please generate one first.")

        return self._current_hangul.roman_chars

    def current_hangul(self) -> Optional[Hangul]:
        return self._current_hangul

    def next_hangul(self) -> Hangul:
        self._current_hangul = random.choice(self._hangul_chars)
        return self._current_hangul

    def score(self) -> Tuple[int, int]:
        return (self._correct_guesses, self._incorrect_guesses)
