from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_choice(self):
        pass