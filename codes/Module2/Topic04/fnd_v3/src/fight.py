import time

def fight(player, monster):
    
    print(f"\n【战斗开始】 {player.name} VS {monster.name}")

    player_power = max(1, player.attack - monster.defense)
    monster_power = max(1, monster.attack - player.defense)

    print(f"你的有效攻击：{player_power}")
    print(f"怪物的有效攻击：{monster_power}")

    round = 1

    while player.is_alive() and monster.is_alive():
        print(f"\n--- 第 {round} 回合 ---")
        round += 1
        time.sleep(1)

        monster.hp -= player_power
        print(f"{player.name} 攻击了 {monster.name}，{monster.name} 剩余血量：{max(0, monster.hp)}")
        if not monster.is_alive():
            print(f"{monster.name} 被击败了！")
            return True
        
        time.sleep(1)

        player.hp -= monster_power
        print(f"{monster.name} 攻击了 {player.name}，{player.name} 剩余血量：{max(0, player.hp)}")
        if not player.is_alive():
            print(f"{player.name} 被击败了！")
            return False
        
        time.sleep(1)