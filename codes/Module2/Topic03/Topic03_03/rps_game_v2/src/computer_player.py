import random
from player import Player

class ComputerPlayer(Player):
    def make_choice(self):
        choice = random.choice(['石头', '剪刀', '布'])
        print(f"{self.name}选择了：{choice}")
        return choice