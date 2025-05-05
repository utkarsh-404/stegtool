import sys
import datetime

class Logger:
    LEVELS = {
        "INFO": "\033[94m[INFO]\033[0m",
        "SUCCESS": "\033[92m[SUCCESS]\033[0m",
        "WARNING": "\033[93m[WARNING]\033[0m",
        "ERROR": "\033[91m[ERROR]\033[0m",
    }

    @staticmethod
    def _timestamp():
        return datetime.datetime.now().strftime("%H:%M:%S")

    @classmethod
    def log(cls, message, level="INFO"):
        prefix = cls.LEVELS.get(level.upper(), "[LOG]")
        print(f"{cls._timestamp()} {prefix} {message}")

    @classmethod
    def info(cls, message):
        cls.log(message, "INFO")

    @classmethod
    def success(cls, message):
        cls.log(message, "SUCCESS")

    @classmethod
    def warning(cls, message):
        cls.log(message, "WARNING")

    @classmethod
    def error(cls, message):
        cls.log(message, "ERROR")
        sys.exit(1)
