from input_handler import get_user_input
from ui import display_menu, show_instructions
from logger import log_write, log_read
from function_cash_flow import function_cash_flow_main
from function_expression import function_expression_main
from function_time_value import function_time_value_main
from user_settings import get_user_settings

def main():
    while True:
        
        # 显示标题与菜单
        display_menu()
        print("-" * 40)
        # 获取用户输入
        user_input = get_user_input()
        print("-" * 40)

        # 处理用户输入
        if user_input == 'q':
            break
        elif user_input == '0':
            show_instructions("0")
        elif user_input == '1':
            function_expression_main()
        elif user_input == '2':
            function_cash_flow_main()
        elif user_input == '3':
            function_time_value_main()
        elif user_input == 'l':
            log_read()
        elif user_input == 's':
            get_user_settings()

if __name__ == "__main__":
    main()