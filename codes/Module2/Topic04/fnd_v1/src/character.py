class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

class Monster(Character):
    def __init__(self, name = "怪物"):
        super().__init__(name=name, hp=20, attack=8, defense=3)

class Player(Character):
    def __init__(self, name = "玩家"):
        super().__init__(name=name, hp=30, attack=7, defense=3)