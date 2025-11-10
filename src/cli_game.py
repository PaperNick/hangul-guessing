from typing import Optional

from src.cli_helpers import ColorMessage
from src.engine import Game
from src.models import Hangul


class CliGame:
    def __init__(self, game: Game) -> None:
        self._game = game

    def _get_user_guess(
        self, hangul: Hangul, prompt_message: Optional[str] = None
    ) -> str:
        if prompt_message is None:
            prompt_message = f'Enter the roman transliteration of "{hangul.char}": '

        print(prompt_message, end="")
        guess = input().strip()

        return guess

    def prompt_new_hangul(self) -> str:
        hangul = self._game.next_hangul()
        return self._get_user_guess(hangul)

    def prompt_current_hangul(self) -> str:
        hangul = self._game.current_hangul() or self._game.next_hangul()
        return self._get_user_guess(hangul)

    def is_guess_correct(self, roman_guess: str) -> bool:
        is_correct = self._game.make_guess(roman_guess)

        if is_correct:
            print(f'{ColorMessage.success("Correct!")}\n')
            self._game.increment_correct()
        else:
            roman_chars = self._game.correct_answer()
            answers = " or ".join(roman_chars)
            print(
                f'{ColorMessage.error("Incorrect.")} The correct answer is -- "{answers}"\n'
            )
            self._game.increment_incorrect()

        return is_correct

    def show_score(self) -> None:
        correct_guesses, incorrect_guesses = self._game.score()
        print(f'{ColorMessage.success("Correct guesses:")} {correct_guesses}')
        print(f'{ColorMessage.error("Incorrect guesses:")} {incorrect_guesses}\n')

    def quit(self) -> None:
        print("Thanks for playing! Your score is:")
        self.show_score()
        quit_game()


def quit_game(*args, **kwargs) -> None:
    exit()


def main() -> None:
    print("Welcome to the Hangul guessing game.")
    print("Enter the roman transliteration of the hangul which is shown.")
    print('To view your score type "score"')
    print('Press "q" to quit at any time.\n')

    hangul_chars = Hangul.load_chars()
    game = Game(hangul_chars)
    cli_game = CliGame(game)

    command_to_action = {
        "q": cli_game.quit,
        "quit": cli_game.quit,
        "score": cli_game.show_score,
    }

    previous_user_input = None
    current_user_input = None
    while True:
        if previous_user_input in command_to_action:
            current_user_input = cli_game.prompt_current_hangul()
        else:
            current_user_input = cli_game.prompt_new_hangul()

        if current_user_input in command_to_action:
            action = command_to_action[current_user_input]
            action()
        else:
            cli_game.is_guess_correct(current_user_input)

        previous_user_input = current_user_input
