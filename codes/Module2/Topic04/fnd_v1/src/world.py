from character import Player, Monster
from item import Sword, Shield, Potion
from fight import fight

class World:

    def __init__(self, map_file):
        self.map = []
        self.player = Player()
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
