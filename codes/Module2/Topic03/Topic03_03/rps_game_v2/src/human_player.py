import json
from config import Config
from player import Player

class HumanPlayer(Player):

    def __init__(self, name=None):
        # 继承父类的初始化方法
        super().__init__(name)
        # 初始化玩家名称与状态，以下代码比较复杂，其实可以封装为一个方法
        if name is None:
            self.name = input("请输入玩家名称：").strip()
        else:
            self.name = name
        self.players_info = self.load_players_info()
        if self.name in self.players_info:
            use_existing = input(f"玩家名称'{self.name}'已存在，是否使用该名称对应的玩家信息？（y/n）(默认为否)：").strip().lower()
            if use_existing in ['y', 'yes', '是']:
                self.stats = self.players_info[self.name]
            else:
                self.stats = {"胜利": 0, "失败": 0, "平局": 0}
        else:
            self.stats = {"胜利": 0, "失败": 0, "平局": 0}
    
    def load_players_info(self):
        with open(f'{Config.PATH_UI}/player.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    def make_choice(self):
        while True:
            choice = input(f"{self.name}，请输入你的选择（石头/剪刀/布）：")
            if choice in ['石头', '剪刀', '布']:
                break
            else:
                print("无效的选择，请重新输入。")
        print(f"{self.name}选择了：{choice}")
        return choice