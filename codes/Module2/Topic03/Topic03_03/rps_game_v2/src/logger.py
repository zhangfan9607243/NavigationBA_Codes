from config import Config
import datetime

class Logger:
    def __init__(self, path):
        self.path = path

    def log_read(self):
        with open(f"{self.path}/game_log.txt", "r", encoding="utf-8") as file:
            logs = file.read()
        print("游戏记录：")
        print(logs)
        
    def log_write(self, content):
        with open(f"{self.path}/game_log.txt", "a", encoding="utf-8") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            content = f"""[{timestamp}]\n{content}\n"""
            file.write(content + "\n")

if __name__ == "__main__":
    logger = Logger(Config.PATH_LOG)
    log_content = "游戏模式：测试模式\n游戏结果：玩家出布，电脑出石头，玩家胜利"
    logger.log_write(log_content)
    logger.log_read()