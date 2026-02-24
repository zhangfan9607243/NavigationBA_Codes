from config import Config
import datetime

class Logger:

    @staticmethod
    def log_write(message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(f"{Config.PATH_LOG}/game.log", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}]\n{message}\n")
    
    @staticmethod
    def log_read():
        with open(f"{Config.PATH_LOG}/game.log", "r", encoding="utf-8") as f:
            return f.read()