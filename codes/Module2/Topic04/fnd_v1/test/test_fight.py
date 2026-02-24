from config_test import *
from character import Player, Monster
from item import Sword, Shield, Potion 
from fight import fight

def test_fight():
    
    player = Player(name="测试玩家")
    monster = Monster(name="测试怪物")

    result = fight(player, monster)

    if result:
        print("玩家获胜！")
    else:
        print("怪物获胜！")

    print(f"战斗结束后，玩家血量：{player.hp}, 怪物血量：{monster.hp}")

if __name__ == "__main__":
    test_fight()