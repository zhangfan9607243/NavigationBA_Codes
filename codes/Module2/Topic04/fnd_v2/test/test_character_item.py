from config_test import *
from character import Player, Monster
from item import Sword, Shield, Potion 

def test_character_item():
    
    player = Player(name="测试玩家")

    sword = Sword()
    print(f"使用剑前，玩家攻击力：{player.attack}")
    sword.apply(player)
    print(f"使用剑后，玩家攻击力：{player.attack}")

    shield = Shield()
    print(f"使用盾牌前，玩家防御力：{player.defense}")
    shield.apply(player)
    print(f"使用盾牌后，玩家防御力：{player.defense}")

    potion = Potion()
    print(f"使用生命药水前，玩家血量：{player.hp}")
    potion.apply(player)
    print(f"使用生命药水后，玩家血量：{player.hp}")

if __name__ == "__main__":
    test_character_item()