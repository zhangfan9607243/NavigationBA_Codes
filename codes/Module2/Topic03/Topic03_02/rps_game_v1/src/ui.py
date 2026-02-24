from config import Config

class UI:
    def __init__(self, path):
        self.path = path

    def display_title(self):
        with open(f"{self.path}/title.txt", "r", encoding="utf-8") as file:
            title = file.read()
        print(title)

    def display_menu(self):
        with open(f"{self.path}/menu.txt", "r", encoding="utf-8") as file:
            menu = file.read()
        print(menu)

    def display_rules(self):
        with open(f"{self.path}/rules.txt", "r", encoding="utf-8") as file:
            rules = file.read()
        print(rules)

if __name__ == "__main__":
    ui = UI(Config.PATH_UI)
    ui.display_title()
    ui.display_menu()
    ui.display_rules()