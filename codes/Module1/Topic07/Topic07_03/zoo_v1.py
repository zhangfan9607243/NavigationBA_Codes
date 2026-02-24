while True:
    
    # TODO: 展示一个漂亮一点的标题

    print("欢迎来到动物园！请选择你想查看的动物：")
    print("输入 '1'：看骆驼")
    print("输入 '2'：看牛")
    print("输入 '3'：看马")
    print("输入 'q'：退出程序")

    while True:
        user_input = input("请输入你的选择: ")
        if user_input in ['1', '2', '3', 'q']:
            break
        else:
            print("输入有误，请重新输入")

    if user_input == '1':
        # TODO: 展示骆驼
        pass
    elif user_input == '2':
        # TODO: 展示牛
        pass
    elif user_input == '3':
        # TODO: 展示马
        pass
    elif user_input == 'q':
        print("感谢你的访问，欢迎下次再来！")
        break