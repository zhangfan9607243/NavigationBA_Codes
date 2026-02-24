from animal_viewer import animal_info

def get_user_input():
    # 生成有效输入列表
    valid_inputs = list(animal_info.keys()) + ['q']
    while True:
        user_input = input("请输入您的选择: ")
        if user_input in valid_inputs:
            break
        else:
            print("输入有误，请重新输入")
    return user_input

if __name__ == "__main__":
    choice = get_user_input()
    print(choice)