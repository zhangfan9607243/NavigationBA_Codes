from config import PATH_PREFIX

def display_menu():
    with open(f"{PATH_PREFIX}data/title.txt", "r", encoding="utf-8") as f:
        title = f.read()
    print(title)
    print("0. 使用说明")
    print("1. 算式计算")
    print("2. 现金流量计算")
    print("3. 时间价值计算")
    print("l. 查看计算历史")
    print("s. 用户设置")
    print("q. 退出")

def show_instructions(function_key="0"):
    # 建立功能与说明文件的映射关系
    function_info = {
        "0": {
            "description": "使用说明",
            "instruction_file": "data/instructions/instructions_overall.txt"
        },
        "1": {
            "description": "算式计算",
            "instruction_file": "data/instructions/instructions_expression.txt"
        },
        "2": {
            "description": "现金流量计算",
            "instruction_file": "data/instructions/instructions_cash_flow.txt"
        },
        "3": {
            "description": "时间价值计算",
            "instruction_file": "data/instructions/instructions_time_value.txt"
        }
    }
    # 读取对应功能的说明文件
    instruction_file = function_info[function_key]["instruction_file"]
    with open(f"{PATH_PREFIX}{instruction_file}", "r", encoding="utf-8") as f:
        instructions = f.read()
    # 显示说明内容    
    print(instructions)
    # 提示按任意键继续
    input("输入任意内容返回上级菜单：")


if __name__ == "__main__":
    # display_menu()
    show_instructions("0")
    show_instructions("1")
    show_instructions("2")
    show_instructions("3")