from config_test import *
from computer_player import ComputerPlayer

def test_computer_player_make_choice():
    player = ComputerPlayer("电脑玩家")
    choice = player.make_choice()
    
if __name__ == "__main__":
    test_computer_player_make_choice()