def get_user_input():
    while True:
        user_input = input("请输入你的选择: ")
        if user_input in ['0', '1', '2', '3', 'l', 'q']:
            break
        else:
            print("输入有误，请重新输入")
    return user_input

if __name__ == "__main__":
    get_user_input()