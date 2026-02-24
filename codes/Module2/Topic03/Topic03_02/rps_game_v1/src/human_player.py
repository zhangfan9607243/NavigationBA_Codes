from player import Player

class HumanPlayer(Player):
    def make_choice(self):
        while True:
            choice = input(f"{self.name}，请输入你的选择（石头/剪刀/布）：")
            if choice in ['石头', '剪刀', '布']:
                break
            else:
                print("无效的选择，请重新输入。")
        print(f"{self.name}选择了：{choice}")
        return choice