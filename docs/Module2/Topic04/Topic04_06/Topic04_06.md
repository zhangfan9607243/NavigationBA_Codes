# Topic 4.6 - 游戏改进与扩展 - 升级 v3 版本

首先，我们将 `fnd_v2` 版本复制一份，命名为 `fnd_v3`，作为我们接下来进行功能升级的基础版本，大家记得改配置文件中的路径。

我们在本次升级中，主要想要实现的功能是玩家的等级与经验系统：

- 在一般的 RPG 游戏中，玩家通过击败怪物可以获得经验值，积累一定的经验值后，玩家就可以升级，提升自己的等级，从而获得更高的属性加成和技能
- 由于我们的地图中怪物数量比较少，所以我们先把升级阈值设置低一些，方便测试

## 1. 实现等级和经验值属性

等级和经验值肯定是作为属性实现在类中的：

- 这两个属性，可以实现在 `Character` 类中，也可以实现在 `Player` 类中
- 如果实现在 `Character` 类中，那么怪物也会有等级和经验值属性，实现在 `Player` 类中，则只有玩家有等级和经验值属性
- 具体选择哪种方式，可以根据游戏设计需求来决定，这里我们就选择实现在 `Character` 类中，方便后续我们给怪物也添加等级和经验值属性
- 虽然我们这次不使用怪物的等级和经验值属性，但同学们如果有兴趣，可以在自己拓展项目时，思考如何利用怪物的等级和经验值属性，来丰富游戏玩法

在代码实现这部分：

- 首先，在 `Character` 类中添加等级和经验值属性比较简单，我们只需要在 `__init__` 方法中添加两个新的属性 `level` 和 `experience` 即可
- 升级的逻辑稍微复杂一点：

    - 我们需要定义一个升级的阈值表，记录到达每个等级所需的经验值，这个是可以根据游戏需求修改的，比方说我们使用一个字典：

    ```python
    level_map = {
            1: 0,
            2: 10,
            3: 20,
            4: 30,
            5: 40,
            6: 50,
            7: 60,
            8: 70,
            9: 80,
            10: 90
        }
    ```

    - 当玩家获得经验值后，我们需要检查当前经验值是否达到了下一个等级的阈值，如果达到了，就进行升级
    
        - 这个稍微复杂一些，我们应该按照经验表，从后往前检查，看看当前经验值是否达到了下一个等级的阈值，这样是为了保证有可能一次获得大量经验值时，可以直接升级多个等级
        - 比方说，当前玩家等级是 1，经验值是 0，如果一次获得了 35 点经验值，那么玩家应该直接升级到 4 级，而不是只升级到 2 级
        - 并且升级还有个条件，就是最高等级不能超过 10 级，当然最高等级也是可以根据需求修改的
    
    - 如果升级，我们需要提升玩家的属性，比如生命值、攻击力、防御力等，这些提升的数值也是可以根据需求调整的

```python
# src/character.py
class Character:
    def __init__(self, name: str, hp: int, attack: int, defense: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.level = 1
        self.experience = 0

    def is_alive(self):
        return self.hp > 0
    
    def level_up(self, exp):

        level_map = {
            1: 0,
            2: 10,
            3: 20,
            4: 30,
            5: 40,
            6: 50,
            7: 60,
            8: 70,
            9: 80,
            10: 90
        }

        self.experience += exp

        # 计算获得经验后的等级
        level_before = self.level
        for lvl in range(max(level_map.keys()), 0, -1):
            if self.experience >= level_map[lvl]:
                level_after = lvl
                break
        
        # 检查是否升级
        if level_after > level_before:
            self.level = level_after
            self.hp += 10
            self.attack += 2
            self.defense += 1
            print(f"{self.name} 升级了！当前等级：{self.level}")

class Monster(Character):
    def __init__(self, name: str = "怪物"):
        super().__init__(name=name, hp=20, attack=8, defense=3)

class Player(Character):
    def __init__(self, name: str = "玩家"):
        super().__init__(name=name, hp=30, attack=7, defense=3)
```

之后，我们在测试代码中，测试一下等级和经验值系统是否正常工作：

```python
# tests/test_character_item.py
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
```

运行一下测试代码，看看输出结果，可以看到经验和等级系统可以正常运行：

```text
等级：1, 经验值：0 血量：30, 攻击力：7, 防御力：3
玩家 升级了！当前等级：2
等级：2, 经验值：10 血量：40, 攻击力：9, 防御力：4
玩家 升级了！当前等级：3
等级：3, 经验值：25 血量：50, 攻击力：11, 防御力：5
玩家 升级了！当前等级：6
等级：6, 经验值：55 血量：60, 攻击力：13, 防御力：6
玩家 升级了！当前等级：10
等级：10, 经验值：255 血量：70, 攻击力：15, 防御力：7
等级：10, 经验值：455 血量：70, 攻击力：15, 防御力：7
```

## 2. 在战斗中获得经验值

接下来，我们需要在战斗中实现击败怪物后，玩家获得经验值的功能：

- 这段代码我们直接在 `World` 类的 `move_player` 方法中实现
- 逻辑比较简单，就是在玩家击败怪物后，调用玩家的 `level_up` 方法，传入一个经验值参数即可
- 这个经验值参数，可以根据游戏设计需求来决定，这里我们就简单地设置为 10 点经验值

```python
# src/world.py
import json
from config import Config
from character import Player, Monster
from item import Sword, Shield, Potion
from fight import fight

class World:

    ...
    
    def move_player(self, dx, dy):

        ...

        # 怪物：踩到触发战斗
        if (nx, ny) in self.monsters:
            monster = self.monsters[(nx, ny)]
            win = fight(self.player, monster)
            # 如果玩家赢了
            if win:
                print("怪物被击败！")
                del self.monsters[(nx, ny)]
                # 玩家获得经验值
                self.player.level_up(10)
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
        
        ...
    
    ...

```

之后，我们再次运行测试代码，看看玩家击败怪物后，是否可以获得经验值并升级，这里我们直接使用之前的世界类的测试代码：

```python
# tests/test_world.py
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

    world = World(f"{Config.PATH_DATA}/map/map_tiny.txt", "玩家")  # 这里需要加入玩家名称
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

    commands_win = ["右", "右（剑）", "下", "右（盾）", "下（怪）", "左", "左", "左（血）", "右", "右", "右", "右", "右", "右（怪）", "右", "右（怪）"]
    commands_los = ["下", "右", "下", "右", "右（怪）", "右", "右", "右（怪）", "右", "右", "右（怪）"]

    print("===== 测试玩家获胜 =====")
    test_world(commands_win)
    # print()
    # print("===== 测试玩家失败 =====")
    # test_world(commands_los)
```

运行结果如下，可以看到，三次战斗后，玩家的等级从 1 级提升到了 4 级，说明经验值和升级系统工作正常：

```text
===== 测试玩家获胜 =====
############
#P.S^^^^^^^#
#...D..~~~~#
#H..M..M..M#
############

当前命令：右
############
#.PS^^^^^^^#
#...D..~~~~#
#H..M..M..M#
############

当前命令：右（剑）
你捡到了剑，攻击力为： 10 点！
############
#..P^^^^^^^#
#...D..~~~~#
#H..M..M..M#
############

当前命令：下
############
#...^^^^^^^#
#..PD..~~~~#
#H..M..M..M#
############

当前命令：右（盾）
你捡到了盾牌，防御力为： 6 点！
############
#...^^^^^^^#
#...P..~~~~#
#H..M..M..M#
############

当前命令：下（怪）

【战斗开始】 玩家 VS 怪物
你的有效攻击：7
怪物的有效攻击：2

--- 第 1 回合 ---
玩家 攻击了 怪物，怪物 剩余血量：13
怪物 攻击了 玩家，玩家 剩余血量：28

--- 第 2 回合 ---
玩家 攻击了 怪物，怪物 剩余血量：6
怪物 攻击了 玩家，玩家 剩余血量：26

--- 第 3 回合 ---
玩家 攻击了 怪物，怪物 剩余血量：0
怪物 被击败了！
怪物被击败！
玩家 升级了！当前等级：2
############
#...^^^^^^^#
#......~~~~#
#H..P..M..M#
############

当前命令：左
############
#...^^^^^^^#
#......~~~~#
#H.P...M..M#
############

当前命令：左
############
#...^^^^^^^#
#......~~~~#
#HP....M..M#
############

当前命令：左（血）
你捡到了生命药水，生命值为： 46 点！
############
#...^^^^^^^#
#......~~~~#
#P.....M..M#
############

当前命令：右
############
#...^^^^^^^#
#......~~~~#
#.P....M..M#
############

当前命令：右
############
#...^^^^^^^#
#......~~~~#
#..P...M..M#
############

当前命令：右
############
#...^^^^^^^#
#......~~~~#
#...P..M..M#
############

当前命令：右
############
#...^^^^^^^#
#......~~~~#
#....P.M..M#
############

当前命令：右
############
#...^^^^^^^#
#......~~~~#
#.....PM..M#
############

当前命令：右（怪）

【战斗开始】 玩家 VS 怪物
你的有效攻击：9
怪物的有效攻击：1

--- 第 1 回合 ---
玩家 攻击了 怪物，怪物 剩余血量：11
怪物 攻击了 玩家，玩家 剩余血量：45

--- 第 2 回合 ---
玩家 攻击了 怪物，怪物 剩余血量：2
怪物 攻击了 玩家，玩家 剩余血量：44

--- 第 3 回合 ---
玩家 攻击了 怪物，怪物 剩余血量：0
怪物 被击败了！
怪物被击败！
玩家 升级了！当前等级：3
############
#...^^^^^^^#
#......~~~~#
#......P..M#
############

当前命令：右
############
#...^^^^^^^#
#......~~~~#
#.......P.M#
############

当前命令：右
############
#...^^^^^^^#
#......~~~~#
#........PM#
############

当前命令：右（怪）

【战斗开始】 玩家 VS 怪物
你的有效攻击：11
怪物的有效攻击：1

--- 第 1 回合 ---
玩家 攻击了 怪物，怪物 剩余血量：9
怪物 攻击了 玩家，玩家 剩余血量：53

--- 第 2 回合 ---
玩家 攻击了 怪物，怪物 剩余血量：0
怪物 被击败了！
怪物被击败！
玩家 升级了！当前等级：4

玩家获胜，游戏结束。
```

到这里，我们就完成了经验值和等级系统的升级

- 同学们可以自行在游戏主程序中测试一下经验值和等级系统的功能
- 大家还可以尝试自己修改经验值阈值表，或者修改升级时属性提升的数值，来体验不同的游戏平衡性设计
- 当然，目前我们手头的地图都比较简单，怪物比较少，大家也可以尝试自己设计更复杂的地图，增加更多的怪物和道具，来丰富游戏玩法

## 3. 项目小结

最后，我们来对整个勇士与地下城游戏项目进行一个小结：

- 在项目开始前，我们先通过最基本的游戏玩法，设计了各个类的基本结构和功能，并且先实现了简单的主程序框架和辅助类
- 之后，我们完善了游戏的各个功能模块，包括地图、角色、道具和战斗等逻辑：

    - 角色、道具、以及战斗的实现都很直观
    - 地图类中，角色移动方法的实现稍微复杂一些，但是我们只要梳理清楚，角色每移动一步需要检查哪些条件，做哪些处理，就能理清思路，完成代码实现
    - 其实大家可以发现，地图类相当于是整个游戏的核心，它协调了角色、道具和战斗等各个模块的工作，是游戏运行的关键

- 最后，我们将所有模块集合到主程序，使玩家可以通过命令行与游戏进行交互，完成整个游戏的流程
- 在项目结束后，我们还对游戏进行了功能升级和扩展，增加了玩家系统，以及经验值和等级系统

我们在课堂上对这个项目的演示就到此为止了，同学们课后可以自己丰富和扩展这个项目，，尝试实现更多有趣的功能，比如：

- 增加不同种类的怪物，丰富更多类型的道具
- 设计更复杂的地图，增加地图切换的功能
- 增加金钱和商店系统，让玩家可以购买和出售道具
- 实现存档和读档功能
- 。。。

通过这个项目，在面向流程编程项目：金融计算器项目经历之上，我们体会了更多关于项目开发的流程和方法，这些经验对于我们今后进行更复杂的项目开发会有很大的帮助。
