import json
from enum import IntEnum
from pathlib import Path
from typing import List


HANGUL_CHARS_PATH = Path("src") / "hangul.json"


class Hangul:
    def __init__(self, char: str, roman_chars: List[str]):
        self.char = char
        self.roman_chars = roman_chars

    @classmethod
    def load_chars(cls) -> List["Hangul"]:
        hangul_list = json.loads(HANGUL_CHARS_PATH.read_text())
        return [cls(char=item[0], roman_chars=item[1]) for item in hangul_list]
