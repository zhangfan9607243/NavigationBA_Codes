import json
from config import Config

class UI:

    @staticmethod
    def display_title():
        with open(f"{Config.PATH_DATA}/ui/title.txt", "r", encoding="utf-8") as f:
            title = f.read()
        print(title)

    @staticmethod
    def display_menu():
        with open(f"{Config.PATH_DATA}/ui/menu.txt", "r", encoding="utf-8") as f:
            menu = f.read()
        print(menu)

    @staticmethod
    def display_rule():
        with open(f"{Config.PATH_DATA}/ui/rule.txt", "r", encoding="utf-8") as f:
            rule = f.read()
        print(rule)
    
    @staticmethod
    def display_leaderboard(top_n=10):
        players_file = f"{Config.PATH_DATA}/players.json"
        with open(players_file, 'r', encoding='utf-8') as f:
            players_data = json.load(f)
        # 按分数排序
        sorted_players = sorted(players_data.items(), key=lambda x: x[1], reverse=True)
        print("=============== 排行榜 ===============")
        for i, (name, score) in enumerate(sorted_players[:top_n]):
            print(f"{i+1}. {name} \t - \t {score} 分")
        print("=====================================")