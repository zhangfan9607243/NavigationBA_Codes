from human_player import HumanPlayer
from computer_player import ComputerPlayer
from config import Config
import json

class Game:

    def __init__(self, mode):

        if mode == 'single':
            self.player1 = HumanPlayer()
            self.player2 = ComputerPlayer("电脑")
        elif mode == 'multi':
            self.player1 = HumanPlayer()
            self.player2 = HumanPlayer()
        
        self.player_info = self.load_players_info()
        
        print("请选择游戏轮数：\n1. 一局定胜负\n2. 三局两胜\n3. 五局三胜")
        rounds_choice = input("请输入您的选择（默认为一局定胜负）：").strip()
        if rounds_choice == '2':
            self.rounds = 3
        elif rounds_choice == '3':
            self.rounds = 5
        else:
            self.rounds = 1
        
        print("-" * 30)

    def load_players_info(self):
        with open(f'{Config.PATH_UI}/player.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def play(self):

        # 初始化比分与日志内容
        player1_score = 0
        player2_score = 0
        log_content = ""
        
        # 每轮游戏
        for i in range(1, self.rounds + 1):

            # 轮次开始提示
            rounds_content1 = f"第 {i} 轮开始！"
            print(rounds_content1)
            log_content += rounds_content1 + "\n"

            # 玩家出拳与结果判定
            choice1 = self.player1.make_choice()
            choice2 = self.player2.make_choice()
            result = self.decide(choice1, choice2)
            if result == 1:
                player1_score += 1
            elif result == 2:
                player2_score += 1
            
            # 展示当前轮的结果
            rounds_content2 = f"第 {i} 轮：{self.player1.name} 出了 {choice1}，{self.player2.name} 出了 {choice2}，结果："
            if result == 0:
                rounds_content2 += "平局"
            elif result == 1:
                rounds_content2 += f"{self.player1.name} 获胜"
                # 更新玩家统计信息
                self.update_stats(self.player1, {"胜利": 1, "失败": 0, "平局": 0})
                if isinstance(self.player2, HumanPlayer):
                    self.update_stats(self.player2, {"胜利": 0, "失败": 1, "平局": 0})
            else:
                rounds_content2 += f"{self.player2.name} 获胜"
                # 更新玩家统计信息
                self.update_stats(self.player1, {"胜利": 0, "失败": 1, "平局": 0})
                if isinstance(self.player2, HumanPlayer):
                    self.update_stats(self.player2, {"胜利": 1, "失败": 0, "平局": 0})
            print(rounds_content2)
            log_content += rounds_content2 + "\n"

            # 展示当前轮后的比分
            rounds_content3 = f"第 {i} 轮后的比分：{self.player1.name} {player1_score} vs {player2_score} {self.player2.name}"
            print(rounds_content3)
            log_content += rounds_content3 + "\n"

            print("*" * 30)
        
        # 游戏结束
        game_content1 = "游戏结束！"
        print(game_content1)
        log_content += game_content1 + "\n"

        # 展示最终比分
        game_content2 = f"最终比分：{self.player1.name} {player1_score} vs {player2_score} {self.player2.name}"
        print(game_content2)
        log_content += game_content2 + "\n"

        # 展示最终获胜者
        game_content3 = "最终获胜者："
        if player1_score > player2_score:
            game_content3 += f"{self.player1.name}"
        elif player2_score > player1_score:
            game_content3 += f"{self.player2.name}"
        else:
            game_content3 += "平局！"
        print(game_content3)
        log_content += game_content3 + "\n"

        # 保存玩家统计信息
        self.save_stats(self.player1)
        if isinstance(self.player2, HumanPlayer):
            self.save_stats(self.player2)

        # 返回日志内容
        return log_content

    def decide(self, choice1, choice2):
        if choice1 == choice2:
            return 0
        elif (choice1 == "石头" and choice2 == "剪刀") or (choice1 == "剪刀" and choice2 == "布") or (choice1 == "布" and choice2 == "石头"):
            return 1
        else:
            return 2
    
    def update_stats(self, player, result_stats):
        for key in result_stats:
            player.stats[key] += result_stats[key]
    
    def save_stats(self, player):
        self.player_info[player.name] = player.stats
        with open(f'{Config.PATH_UI}/player.json', 'w', encoding='utf-8') as f:
            json.dump(self.player_info, f, ensure_ascii=False, indent=4)