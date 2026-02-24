from config_test import *
from game import Game

def test_game_single_mode():
    game = Game(mode='single')
    print(game.player1.stats)
    result = game.play()
    print(game.player1.stats)

def test_game_multi_mode():
    game = Game(mode='multi')
    print(game.player1.stats)
    print(game.player2.stats)
    result = game.play()
    print(game.player1.stats)
    print(game.player2.stats)

if __name__ == "__main__":
    print("测试单人模式：")
    test_game_single_mode()
    print()
    print("测试多人模式：")
    test_game_multi_mode()