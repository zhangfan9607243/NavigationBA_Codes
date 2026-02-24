class Character:
    def __init__(self, name: str, hp: int, attack: int, defense: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

class Monster(Character):
    def __init__(self, name: str = "怪物"):
        super().__init__(name=name, hp=20, attack=8, defense=3)

class Player(Character):
    def __init__(self, name: str = "玩家"):
        super().__init__(name=name, hp=30, attack=7, defense=3)