from .tool1 import greet
from .tool2 import farewell

def welcome_and_farewell(name):
    greeting = greet(name)
    goodbye = farewell(name)
    return f"{greeting} ... {goodbye}"

if __name__ == "__main__":
    print(welcome_and_farewell("Alice"))
