# Topic 4.5 - 游戏改进与扩展 - 升级 v2 版本

首先，我们将 `fnd_v1` 版本复制一份，命名为 `fnd_v2`，作为我们接下来进行功能升级的基础版本，大家记得改配置文件中的路径。

本次升级，我们将之前在石头剪刀布游戏中实现过的一个功能移植过来，那就是玩家系统与排行榜功能：

- 这两个功能是紧密相关的，仿照石头剪刀布游戏，我们首先来设计一下这个游戏的分数，我们可以设计地比较简单，就是每击败一个怪物加1分
- 这样，我们存储玩家信息的 `json` 文件就十分简单（这个文件我们就存储在 `data/players.json` 中）：

```json
{
    "测试玩家1": 5,
    "测试玩家2": 3,
    "测试玩家3": 8
}
```

## 1. 加入玩家系统

在刚刚进入游戏时：

- 我们需要玩家输入一个名字，作为玩家的唯一标识，游戏中我们也使用这个名字来作为玩家的称呼
- 如果这个名字在玩家信息 json 文件中已经存在，我们就读取这个玩家的分数
- 如果这个名字不存在，我们就创建一个新的玩家，初始分数为 0 分

首先，我们在主程序 `main.py` 中加入玩家系统的代码，让玩家输入名字这个步骤，我们放在展示标题和菜单中间：

- 我们新增一个 `get_player_name` 方法，专门用来处理玩家名字的输入和玩家信息的读取/创建
- 在获取到玩家名字后，在 `start_game` 方法中，再把玩家名字传递给 `World` 类的实例化，以便在游戏过程中使用玩家名字

```python
# src/main.py
import json
from config import Config
from ui import UI
from world import World
from logger import Logger

class Program:

    def __init__(self):
        self.player_name = None

    def run(self):

        # 记录程序开始
        Logger.log_write("系统日志 -- 程序开始运行")

        # 游戏主循环
        while True:
            
            # 展示标题
            UI.display_title()
            
            # 获取玩家名字
            if self.player_name is None:
                self.player_name = self.get_player_name()
            
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
                        self.start_game(f"{Config.PATH_DATA}/map/map_tiny.txt",)
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
    
    def get_player_name(self):
        # 读取玩家信息文件
        players_file = f"{Config.PATH_DATA}/players.json"
        with open(players_file, 'r', encoding='utf-8') as f:
            players_data = json.load(f)
        # 获取玩家名字
        while True:
            name = input("请输入您的玩家名字：").strip()
            if name != "":
                if name in players_data:
                    print(f"欢迎回来，{name}！您的当前分数是 {players_data[name]} 分。")
                    Logger.log_write(f"系统日志 -- 玩家 {name} 登录，当前分数 {players_data[name]}")
                else:
                    players_data[name] = 0
                    with open(players_file, 'w', encoding='utf-8') as f:
                        json.dump(players_data, f, ensure_ascii=False, indent=4)
                    print(f"欢迎新玩家，{name}！您的初始分数是 0 分。")
                    Logger.log_write(f"系统日志 -- 新玩家 {name} 创建，初始分数 0")
                return name
            else:
                print("玩家名字不能为空，请重新输入！")

    def start_game(self, map_path):

        world = World(map_path, self.player_name)

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
```

在将玩家名字传递给 `World` 类后：

- 我们还需要在 `world.py` 中修改 `World` 类的初始化方法，以接受玩家名字参数，并将其传递给 `Player` 类
- 但是 `Player` 类是不需要修改的，因为我们在创建时，本身就有传递名字参数的设计
- 除此之外，我们还需要在玩家获胜后，更新玩家的分数

```python
# src/world.py
import json
from config import Config
from character import Player, Monster
from item import Sword, Shield, Potion
from fight import fight

class World:

    def __init__(self, map_file, player_name):
        self.map = []
        self.player = Player(player_name)
        self.player_pos = None
        self.monsters = {}
        self.items = {}
        self.map_load(map_file)
        self.find_elements()

    def map_load(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # 行尾的换行符要去掉
                line = line.rstrip('\n')
                self.map.append(list(line))
    
    def map_show(self):
        for row in self.map:
            print("".join(row))

    def find_elements(self):
        for y, row in enumerate(self.map):
            for x, symbol in enumerate(row):
                if symbol == 'P':
                    self.player_pos = (x, y)
                elif symbol == 'M':
                    self.monsters[(x, y)] = Monster()
                elif symbol == 'S':
                    self.items[(x, y)] = Sword()
                elif symbol == 'D':
                    self.items[(x, y)] = Shield()
                elif symbol == 'H':
                    self.items[(x, y)] = Potion()
    
    def move_player(self, dx, dy):
        x, y = self.player_pos
        nx, ny = x + dx, y + dy

        # 障碍物检测：# 边界墙，^ 山，~ 水
        if self.map[ny][nx] in {'#', '^', '~'}:
            block = self.map[ny][nx]
            if block == '#':
                print("前方是边界墙，无法通过。")
            elif block == '^':
                print("前方是高山，无法通过。")
            else:  # '~'
                print("前方是水域，无法通过。")
            return

        # 怪物：踩到触发战斗
        if (nx, ny) in self.monsters:
            monster = self.monsters[(nx, ny)]
            win = fight(self.player, monster)
            # 如果玩家赢了
            if win:
                print("怪物被击败！")
                del self.monsters[(nx, ny)]
                # 更新玩家分数
                players_file = f"{Config.PATH_DATA}/players.json"
                with open(players_file, 'r', encoding='utf-8') as f:
                    players_data = json.load(f)
                players_data[self.player.name] = players_data.get(self.player.name, 0) + 1
                with open(players_file, 'w', encoding='utf-8') as f:
                    json.dump(players_data, f, ensure_ascii=False, indent=4)
            # 如果玩家输了
            else:
                print("你被怪物击败了……")
                return

        # 道具：踩到自动使用
        if (nx, ny) in self.items:
            item = self.items[(nx, ny)]
            item.apply(self.player)
            if isinstance(item, Potion):
                print(f"你捡到了生命药水，生命值为： {self.player.hp} 点！")
            elif isinstance(item, Sword):
                print(f"你捡到了剑，攻击力为： {self.player.attack} 点！")
            elif isinstance(item, Shield):
                print(f"你捡到了盾牌，防御力为： {self.player.defense} 点！")
            del self.items[(nx, ny)]

        # 移动玩家
        self.map[y][x] = '.'
        self.map[ny][nx] = 'P'
        self.player_pos = (nx, ny)
```

我们再次运行 `main.py` ，并且创建一个新的玩家 `张三`，并玩一局游戏，看看效果：

```text
================================
=  ███████╗███╗   ██╗██████╗   =
=  ██╔════╝████╗  ██║██╔══██╗  =
=  █████╗  ██╔██╗ ██║██║  ██║  =
=  ██╔══╝  ██║╚██╗██║██║  ██║  =
=  ██║     ██║ ╚████║██████╔╝  =
=  ╚═╝     ╚═╝  ╚═══╝╚═════╝   =
================================
=          勇士与地下城          =
================================
请输入您的玩家名字：张三
欢迎新玩家，张三！您的初始分数是 0 分。
请选择：
p. 开始游戏
r. 查看规则
q. 退出游戏
----------------------------------------
请输入选项：p
----------------------------------------
请选择游戏难度：
0. 新手（超小地图）
1. 简单（小地图）
2. 普通（中地图）
3. 困难（大地图）
q. 返回主菜单
----------------------------------------
请选择游戏难度：0
----------------------------------------
游戏开始！
使用 w/a/s/d 控制上下左右移动，q 退出本局游戏。
----------------------------------------
############
#P.S^^^^^^^#
#...D..~~~~#
#H..M..M..M#
############
您的指令：d
############
#.PS^^^^^^^#
#...D..~~~~#
#H..M..M..M#
############
您的指令：d
你捡到了剑，攻击力为： 10 点！
############
#..P^^^^^^^#
#...D..~~~~#
#H..M..M..M#
############
您的指令：s
############
#...^^^^^^^#
#..PD..~~~~#
#H..M..M..M#
############
您的指令：d
你捡到了盾牌，防御力为： 6 点！
############
#...^^^^^^^#
#...P..~~~~#
#H..M..M..M#
############
您的指令：s

【战斗开始】 张三 VS 怪物
你的有效攻击：7
怪物的有效攻击：2

--- 第 1 回合 ---
张三 攻击了 怪物，怪物 剩余血量：13
怪物 攻击了 张三，张三 剩余血量：28

--- 第 2 回合 ---
张三 攻击了 怪物，怪物 剩余血量：6
怪物 攻击了 张三，张三 剩余血量：26

--- 第 3 回合 ---
张三 攻击了 怪物，怪物 剩余血量：0
怪物 被击败了！
怪物被击败！
############
#...^^^^^^^#
#......~~~~#
#H..P..M..M#
############
您的指令：a
############
#...^^^^^^^#
#......~~~~#
#H.P...M..M#
############
您的指令：a
############
#...^^^^^^^#
#......~~~~#
#HP....M..M#
############
您的指令：a
你捡到了生命药水，生命值为： 36 点！
############
#...^^^^^^^#
#......~~~~#
#P.....M..M#
############
您的指令：d
############
#...^^^^^^^#
#......~~~~#
#.P....M..M#
############
您的指令：d
############
#...^^^^^^^#
#......~~~~#
#..P...M..M#
############
您的指令：d
############
#...^^^^^^^#
#......~~~~#
#...P..M..M#
############
您的指令：d
############
#...^^^^^^^#
#......~~~~#
#....P.M..M#
############
您的指令：d
############
#...^^^^^^^#
#......~~~~#
#.....PM..M#
############
您的指令：d

【战斗开始】 张三 VS 怪物
你的有效攻击：7
怪物的有效攻击：2

--- 第 1 回合 ---
张三 攻击了 怪物，怪物 剩余血量：13
怪物 攻击了 张三，张三 剩余血量：34

--- 第 2 回合 ---
张三 攻击了 怪物，怪物 剩余血量：6
怪物 攻击了 张三，张三 剩余血量：32

--- 第 3 回合 ---
张三 攻击了 怪物，怪物 剩余血量：0
怪物 被击败了！
怪物被击败！
############
#...^^^^^^^#
#......~~~~#
#......P..M#
############
您的指令：d
############
#...^^^^^^^#
#......~~~~#
#.......P.M#
############
您的指令：d
############
#...^^^^^^^#
#......~~~~#
#........PM#
############
您的指令：d

【战斗开始】 张三 VS 怪物
你的有效攻击：7
怪物的有效攻击：2

--- 第 1 回合 ---
张三 攻击了 怪物，怪物 剩余血量：13
怪物 攻击了 张三，张三 剩余血量：30

--- 第 2 回合 ---
张三 攻击了 怪物，怪物 剩余血量：6
怪物 攻击了 张三，张三 剩余血量：28

--- 第 3 回合 ---
张三 攻击了 怪物，怪物 剩余血量：0
怪物 被击败了！
怪物被击败！
恭喜你，击败了所有怪物，赢得了游戏！
按回车返回主菜单...
================================
=  ███████╗███╗   ██╗██████╗   =
=  ██╔════╝████╗  ██║██╔══██╗  =
=  █████╗  ██╔██╗ ██║██║  ██║  =
=  ██╔══╝  ██║╚██╗██║██║  ██║  =
=  ██║     ██║ ╚████║██████╔╝  =
=  ╚═╝     ╚═╝  ╚═══╝╚═════╝   =
================================
=          勇士与地下城          =
================================
请选择：
p. 开始游戏
r. 查看规则
q. 退出游戏
----------------------------------------
请输入选项：q
----------------------------------------
感谢游玩，期待下次再见！
```

之后，我们再次以 `张三` 玩家身份登录游戏，看看分数是否正确保存：

```text
================================
=  ███████╗███╗   ██╗██████╗   =
=  ██╔════╝████╗  ██║██╔══██╗  =
=  █████╗  ██╔██╗ ██║██║  ██║  =
=  ██╔══╝  ██║╚██╗██║██║  ██║  =
=  ██║     ██║ ╚████║██████╔╝  =
=  ╚═╝     ╚═╝  ╚═══╝╚═════╝   =
================================
=          勇士与地下城          =
================================
请输入您的玩家名字：张三
欢迎回来，张三！您的当前分数是 3 分。
请选择：
p. 开始游戏
r. 查看规则
q. 退出游戏
----------------------------------------
请输入选项：q
----------------------------------------
感谢游玩，期待下次再见！
```

我们还可以打开 `data/players.json` 文件，也可以看到新建的玩家和分数已经成功更新了：

```json
{
    "测试玩家1": 5,
    "测试玩家2": 3,
    "测试玩家3": 8,
    "张三": 3
}
```

# 2. 加入排行榜系统

排行榜系统就比较简单了：

- 只需要读取玩家信息的 `json` 文件，然后按照分数进行排序，最后展示前几名玩家的信息即可
- 这个排行要比石头剪刀布要简单直白一些，因为我们只有分数这个维度，不需要考虑失败或平局等复杂情况
- 这个功能我们就直接在 `ui.py` 中实现了：

```python
# src/ui.py
import json
from config import Config

class UI:

    @staticmethod
    def display_title():
        with open(f"{Config.PATH_DATA}/ui/title.txt", "r", encoding="utf-8") as f:
            title = f.read()
        print(title)

    @staticmethod
    def display_menu():
        with open(f"{Config.PATH_DATA}/ui/menu.txt", "r", encoding="utf-8") as f:
            menu = f.read()
        print(menu)

    @staticmethod
    def display_rule():
        with open(f"{Config.PATH_DATA}/ui/rule.txt", "r", encoding="utf-8") as f:
            rule = f.read()
        print(rule)
    
    @staticmethod
    def display_leaderboard(top_n=10):
        players_file = f"{Config.PATH_DATA}/players.json"
        with open(players_file, 'r', encoding='utf-8') as f:
            players_data = json.load(f)
        # 按分数排序
        sorted_players = sorted(players_data.items(), key=lambda x: x[1], reverse=True)
        print("=============== 排行榜 ===============")
        for i, (name, score) in enumerate(sorted_players[:top_n]):
            print(f"{i+1}. {name} \t - \t {score} 分")
        print("=====================================")
```

- 在 `main.py` 中，我们可以在主菜单中加入一个选项，这个实现就太简单了，我们就不展示了

之后，我们在 `players.json` 文件中添加一些测试玩家数据：

```json
{
    "测试玩家1": 5,
    "测试玩家2": 3,
    "测试玩家3": 8,
    "张三": 3,
    "李四": 10,
    "王五": 7,
    "赵六": 2,
    "牛七": 6,
    "马八": 4,
    "杨九": 9,
    "周十": 1
}
```

最后，我们运行程序，选择查看排行榜选项，看看效果（注意，`markdown` 里可能没有对齐，但是控制台上是对齐了的）：

```text
================================
=  ███████╗███╗   ██╗██████╗   =
=  ██╔════╝████╗  ██║██╔══██╗  =
=  █████╗  ██╔██╗ ██║██║  ██║  =
=  ██╔══╝  ██║╚██╗██║██║  ██║  =
=  ██║     ██║ ╚████║██████╔╝  =
=  ╚═╝     ╚═╝  ╚═══╝╚═════╝   =
================================
=          勇士与地下城          =
================================
请输入您的玩家名字：张三
欢迎回来，张三！您的当前分数是 3 分。
请选择：
p. 开始游戏
r. 查看规则
l. 排行榜
q. 退出游戏
----------------------------------------
请输入选项：l
----------------------------------------
=============== 排行榜 ===============
1. 李四          -       10 分
2. 杨九          -       9 分
3. 测试玩家3     -       8 分
4. 王五          -       7 分
5. 牛七          -       6 分
6. 测试玩家1     -       5 分
7. 马八          -       4 分
8. 测试玩家2     -       3 分
9. 张三          -       3 分
10. 赵六         -       2 分
=====================================
按回车返回主菜单...
================================
=  ███████╗███╗   ██╗██████╗   =
=  ██╔════╝████╗  ██║██╔══██╗  =
=  █████╗  ██╔██╗ ██║██║  ██║  =
=  ██╔══╝  ██║╚██╗██║██║  ██║  =
=  ██║     ██║ ╚████║██████╔╝  =
=  ╚═╝     ╚═╝  ╚═══╝╚═════╝   =
================================
=          勇士与地下城          =
================================
请选择：
p. 开始游戏
r. 查看规则
l. 排行榜
q. 退出游戏
----------------------------------------
请输入选项：q
----------------------------------------
感谢游玩，期待下次再见！
```

至此，我们就完成了游戏的 v2 版本升级，加入了玩家系统与排行榜功能。
