from human_player import HumanPlayer
from computer_player import ComputerPlayer

class Game:

    def __init__(self, mode):
        if mode == 'single':
            self.player1 = HumanPlayer("玩家")
            self.player2 = ComputerPlayer("电脑")
        elif mode == 'multi':
            self.player1 = HumanPlayer("玩家1")
            self.player2 = HumanPlayer("玩家2")

    def play(self):
        choice1 = self.player1.make_choice()
        choice2 = self.player2.make_choice()
        result = self.decide(choice1, choice2)
        return f"{self.player1.name}出了{choice1}，{self.player2.name}出了{choice2}，结果：{result}"

    def decide(self, choice1, choice2):
        if choice1 == choice2:
            return "平局！"
        elif (choice1 == "石头" and choice2 == "剪刀") or (choice1 == "剪刀" and choice2 == "布") or (choice1 == "布" and choice2 == "石头"):
            return f"{self.player1.name}胜利！"
        else:
            return f"{self.player2.name}胜利！"