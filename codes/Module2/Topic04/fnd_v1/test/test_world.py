from config_test import *
from world import World
from config import Config
import time

def test_world(commands):

    """
    测试地图：
    ############
    #P.S^^^^^^^#
    #...D..~~~~#
    #H..M..M..M#
    ############
    """

    world = World(f"{Config.PATH_DATA}/map/map_tiny.txt")
    for command in commands:
        world.map_show()
        print(f"\n当前命令：{command}")
        if "左" in command:
            world.move_player(-1, 0)
        elif "右" in command:
            world.move_player(1, 0)
        elif "上" in command:
            world.move_player(0, -1)
        elif "下" in command:
            world.move_player(0, 1)
        
        if not world.player.is_alive():
            break

        time.sleep(1)
    
    if world.player.is_alive():

        print("\n玩家获胜，游戏结束。")
    else:
        print("\n玩家战败，测试结束。")

if __name__ == "__main__":

    commands_win = ["右", "右（剑）", "下", "右（盾）", "下（怪）", "左", "左", "左（血）", "右", "右", "右", "右", "右", "右（怪）", "右", "右", "右（怪）"]
    commands_los = ["下", "右", "下", "右", "右（怪）", "右", "右", "右（怪）", "右", "右", "右（怪）"]

    print("===== 测试玩家获胜 =====")
    test_world(commands_win)
    print()
    print("===== 测试玩家失败 =====")
    test_world(commands_los)