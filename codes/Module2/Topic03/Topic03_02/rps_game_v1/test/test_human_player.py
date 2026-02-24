from config_test import *
from human_player import HumanPlayer

def test_human_player_make_choice():
    player = HumanPlayer("测试玩家")
    choice = player.make_choice()

if __name__ == "__main__":
    test_human_player_make_choice()