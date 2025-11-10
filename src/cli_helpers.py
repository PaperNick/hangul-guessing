class ColorMessage:
    GREEN = "\033[92m"
    RED = "\033[91m"
    END_COLOR = "\033[0m"

    @classmethod
    def success(cls, msg: str) -> str:
        return f"{cls.GREEN}{msg}{cls.END_COLOR}"

    @classmethod
    def error(cls, msg: str) -> str:
        return f"{cls.RED}{msg}{cls.END_COLOR}"
