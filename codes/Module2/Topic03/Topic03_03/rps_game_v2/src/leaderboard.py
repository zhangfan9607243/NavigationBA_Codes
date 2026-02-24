import json
from config import Config

class Leaderboard:

    def __init__(self):
        self.players_info = self.load_players_info()
    
    def load_players_info(self):
        with open(f'{Config.PATH_UI}/player.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def display_leaderboard(self):
        sorted_players = sorted(self.players_info.items(), key=lambda x: (-x[1]['胜利'], x[1]['失败'], -x[1]['平局']))
        print("排行榜前10名：")
        print("{:<15} \t {:<6} \t {:<6} \t {:<6}".format("玩家名称", "胜利", "失败", "平局"))
        print("-" * 65)
        for i, (name, stats) in enumerate(sorted_players[:10], start=1):
            print("{:<15} \t {:<6} \t {:<6} \t {:<6}".format(name, stats['胜利'], stats['失败'], stats['平局']))

if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.display_leaderboard()