from config import Config
from ui import UI
from world import World
from logger import Logger

class Program:

    def run(self):

        # 记录程序开始
        Logger.log_write("系统日志 -- 程序开始运行")

        # 游戏主循环
        while True:
            
            # 展示标题和菜单
            UI.display_title()
            UI.display_menu()
            print("-" * 40)

            # 获取玩家输入
            choice = input("请输入选项：")
            print("-" * 40)

            if choice == "p":

                while True:
                    # 展示游戏难度选择菜单
                    print("请选择游戏难度：")
                    print("0. 新手（超小地图）")
                    print("1. 简单（小地图）")
                    print("2. 普通（中地图）")
                    print("3. 困难（大地图）")
                    print("q. 返回主菜单")
                    print("-" * 40)
                    choice_play = input("请选择游戏难度：").strip()
                    print("-" * 40)
                    # 根据选择启动游戏
                    if choice_play == "0":
                        Logger.log_write("系统日志 -- 游戏开始，难度：新手（超小地图）")
                        self.start_game(f"{Config.PATH_DATA}/map/map_tiny.txt")
                        Logger.log_write("系统日志 -- 游戏结束，难度：新手（超小地图）")
                        break # 默认跳出难度选择循环，返回主菜单
                    elif choice_play == "1":
                        Logger.log_write("系统日志 -- 游戏开始，难度：简单（小地图）")
                        self.start_game(f"{Config.PATH_DATA}/map/map_small.txt")
                        Logger.log_write("系统日志 -- 游戏结束，难度：简单（小地图）")
                        break # 默认跳出难度选择循环，返回主菜单
                    elif choice_play == "2":
                        Logger.log_write("系统日志 -- 游戏开始，难度：普通（中地图）")
                        self.start_game(f"{Config.PATH_DATA}/map/map_medium.txt")
                        Logger.log_write("系统日志 -- 游戏结束，难度：普通（中地图）")
                        break # 默认跳出难度选择循环，返回主菜单
                    elif choice_play == "3":
                        Logger.log_write("系统日志 -- 游戏开始，难度：困难（大地图）")
                        self.start_game(f"{Config.PATH_DATA}/map/map_large.txt")
                        Logger.log_write("系统日志 -- 游戏结束，难度：困难（大地图）")
                        break # 默认跳出难度选择循环，返回主菜单
                    elif choice_play == "q":
                        break # 返回主菜单
                    else:
                        print("无效的选项，请重新输入！")
            
            elif choice == "r":
                UI.display_rule()

            elif choice == "q":
                print("感谢游玩，期待下次再见！")
                Logger.log_write("系统日志 -- 程序结束运行")
                break
    
    def start_game(self, map_path):

        world = World(map_path)

        print("游戏开始！")
        print("使用 w/a/s/d 控制上下左右移动，q 退出本局游戏。")
        print("-" * 40)
        
        while True:

            world.map_show()
            
            cmd = input("您的指令：").strip().lower()

            if cmd == 'q':
                print("你退出了本次游戏。")
                Logger.log_write("游戏日志 -- 玩家退出游戏")
                break
            elif cmd == 'w':
                world.move_player(0, -1)
            elif cmd == 's':
                world.move_player(0, 1)
            elif cmd == 'a':
                world.move_player(-1, 0)
            elif cmd == 'd':
                world.move_player(1, 0)
            else:
                print("无效的命令，请重新输入！")
            
            if not world.player.is_alive():
                print("你的生命值归零，游戏结束。")
                Logger.log_write("游戏日志 -- 游戏结束，玩家失败")
                break
            
            if world.monsters == {}:
                print("恭喜你，击败了所有怪物，赢得了游戏！")
                Logger.log_write("游戏日志 -- 游戏结束，玩家胜利")
                break

        input("按回车返回主菜单...")

if __name__ == "__main__":
    program = Program()
    program.run()