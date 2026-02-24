from config_test import *
from human_player import HumanPlayer

def test_human_player_make_choice():
    player = HumanPlayer()
    print(player.stats)
    choice = player.make_choice()
    print(f"玩家选择是：{choice}")

if __name__ == "__main__":
    test_human_player_make_choice()
    print()
    test_human_player_make_choice()
    print()
    test_human_player_make_choice()