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