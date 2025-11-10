from signal import signal, SIGINT

from src.cli_game import main, quit_game


if __name__ == '__main__':
    signal(SIGINT, quit_game)

    try:
        main()
    except EOFError:
        # Ctrl + D has been pressed
        quit_game()
