ascii_camel = r"""
        _
    .--' |
   /___^ |     .--.
       ) |    /    \
      /  |  /`      '.
     |   '-'    /     \
     \         |      |\
      \    /   \      /\|
       \  /'----`\   /
       |||       \\ |
       ((|        ((|
       |||        |||
      //_(       //_(
"""

ascii_cow = r"""
    ^__^
    (oo)\_______
    (__)\       )\/\
        ||----w |
        ||     ||
"""

ascii_horse = r"""
                                 |\    /|
                              ___| \,,/_/
                           ---__/ \/    \
                          __--/    (D)(D)\
                          _ -/    (_      \
                         // /       \_ /  -\
   __-------_____--___--/           / \_ O o)
  /                                 /   \__/
 /                                 /
||          )                   \_/\
||         /              _      /  |
| |      /--______      ___\    /\  :
| /   __-  - _/   ------    |  |   \ \
 |   -  -   /                | |     \ )
 |  |   -  |                 | )     | |
  | |    | |                 | |    | |
  | |    < |                 | |   |_/
  < |    /__\                <  \
  /__\                       /___\
"""

assic_title = r"""
    *****************************
    *       欢迎来到动物园       *
    *****************************
"""

while True:
    
    print(assic_title)

    print("请选择你想查看的动物：")
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
        print("这是一头骆驼，请看：")
        print(assic_camel)
        input("输入任意内容退回到菜单")
    elif user_input == '2':
        print("这是一头牛，请看：")
        print(ascii_cow)
        input("输入任意内容退回到菜单")
    elif user_input == '3':
        print("这是一匹马，请看：")
        print(ascii_horse)
        input("输入任意内容退回到菜单")
    elif user_input == 'q':
        print("感谢你的访问，欢迎下次再来！")
        break