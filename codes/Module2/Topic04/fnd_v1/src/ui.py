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