from logger import logger
from ui import display_title_menu
from input_handler import get_user_input
from animal_viewer import display_animal, animal_info

def main():
    
    logger("程序启动")

    while True:
        try:
            display_title_menu()
            
            user_input = get_user_input()
            
            if user_input == 'q':
                logger("程序退出")
                print("感谢使用动物园程序，再见！")
                break
            elif user_input in list(animal_info.keys()):
                display_animal(user_input)
                logger(f"用户查看动物{user_input}")
        
        except Exception as e:
            logger(f"程序错误: {e}")
            print("程序出现错误，请重试。")

if __name__ == "__main__":
    main()
else:
    logger("开发者测试主程序")