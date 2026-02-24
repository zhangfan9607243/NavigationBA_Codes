decimal_places = 4
money_symbol = "¥"

def set_decimal_places():
    global decimal_places
    print("设置小数点位数：")
    print(f"当前小数点位数设置为：{decimal_places}")
    while True:
        try:
            decimal_places_new = int(input("请输入新的小数点位数（0-10之间的整数）："))
            if 0 <= decimal_places_new <= 10:
                decimal_places = decimal_places_new
                print(f"小数点位数已更新为：{decimal_places}")
                break
            else:
                print("输入有误，请输入0到10之间的整数。")
        except Exception:
            print("输入有误，请输入有效的整数。")

def set_money_symbol():
    global money_symbol
    money_symbol_valid_list = ['¥', '$', '€', '£']
    print("设置金额符号：")
    print(f"当前金额符号设置为：{money_symbol}")
    while True:
        try:
            money_symbol_new = input(f"请输入新的金额符号（{'、'.join(money_symbol_valid_list)}）：").strip()
            if money_symbol_new in money_symbol_valid_list:
                money_symbol = money_symbol_new
                print(f"金额符号已更新为：{money_symbol}")
                break
            else:
                print("输入有误，请输入有效的金额符号。")
        except Exception:
            print("输入有误，请输入有效的金额符号。")

def get_user_settings():
    while True:
        print("-" * 40)
        print("用户设置：")
        print("1. 设置小数点位数")
        print("2. 设置金额符号")
        print("q. 返回主菜单")
        print("-" * 40)
        choice = input("请输入您的选择：")
        print("-" * 40)
        if choice == '1':
            set_decimal_places()
        elif choice == '2':
            set_money_symbol()
        elif choice == 'q':
            break
        else:
            print("输入有误，请重新输入。")

# 提供获取当前小数点位数的函数
def get_decimal_places():
    return decimal_places

# 提供获取当前金额符号的函数
def get_money_symbol():
    return money_symbol

if __name__ == "__main__":
    get_user_settings()