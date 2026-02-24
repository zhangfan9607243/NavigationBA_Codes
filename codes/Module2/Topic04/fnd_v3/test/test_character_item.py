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

def test_level_up():
    player = Player()
    print(f"等级：{player.level}, 经验值：{player.experience} 血量：{player.hp}, 攻击力：{player.attack}, 防御力：{player.defense}")
    player.level_up(10)
    print(f"等级：{player.level}, 经验值：{player.experience} 血量：{player.hp}, 攻击力：{player.attack}, 防御力：{player.defense}")
    player.level_up(15)
    print(f"等级：{player.level}, 经验值：{player.experience} 血量：{player.hp}, 攻击力：{player.attack}, 防御力：{player.defense}")
    player.level_up(30)
    print(f"等级：{player.level}, 经验值：{player.experience} 血量：{player.hp}, 攻击力：{player.attack}, 防御力：{player.defense}")
    player.level_up(200)
    print(f"等级：{player.level}, 经验值：{player.experience} 血量：{player.hp}, 攻击力：{player.attack}, 防御力：{player.defense}")
    player.level_up(200)
    print(f"等级：{player.level}, 经验值：{player.experience} 血量：{player.hp}, 攻击力：{player.attack}, 防御力：{player.defense}")

if __name__ == "__main__":
    # test_character_item()
    test_level_up()