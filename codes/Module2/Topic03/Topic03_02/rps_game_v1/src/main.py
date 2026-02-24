from config import Config
from logger import Logger
from ui import UI
from game import Game
from human_player import HumanPlayer
from computer_player import ComputerPlayer

class Program:
    def __init__(self):
        self.logger = Logger(Config.PATH_LOG)
        self.ui = UI(Config.PATH_UI)

    def run(self):

        while True:
            self.ui.display_title()
            self.ui.display_menu()
            choice = input("请输入您的选择：")
            if choice == '1':
                game = Game(mode='single')
                result = game.play()
                print(result)
                self.logger.log_write(result)
            elif choice == '2':
                game = Game(mode='multi')
                result = game.play()
                print(result)
                self.logger.log_write(result)
            elif choice == 'h':
                self.ui.display_rules()
            elif choice == 'l':
                self.logger.log_read()
            elif choice == 'q':
                print("感谢游玩，再见！")
                break
            else:
                print("无效选择，请重新输入。")

if __name__ == "__main__":
    program = Program()
    program.run()