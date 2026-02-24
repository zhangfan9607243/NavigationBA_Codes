from config_test import *
from game import Game

def test_game_single_mode():
    game = Game(mode='single')
    result = game.play()
    print(result)

def test_game_multi_mode():
    game = Game(mode='multi')
    result = game.play()
    print(result)

if __name__ == "__main__":
    print("测试单人模式：")
    test_game_single_mode()
    print("测试多人模式：")
    test_game_multi_mode()