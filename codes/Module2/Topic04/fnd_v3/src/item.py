from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply(self, player):
        pass

class Potion(Item):
    def __init__(self):
        super().__init__(name="生命药水")

    def apply(self, player):
        player.hp += 10

class Shield(Item):
    def __init__(self):
        super().__init__(name="盾牌")
        
    def apply(self, player):
        player.defense += 3

class Sword(Item):
    def __init__(self):
        super().__init__(name="剑")

    def apply(self, player):
        player.attack += 3