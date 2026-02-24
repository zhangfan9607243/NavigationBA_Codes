from config import PATH_PREFIX
from animal_viewer import animal_info

def display_title_menu():
    # 读取标题文件
    with open(f"{PATH_PREFIX}/data/title.txt", "r", encoding="utf-8") as f:
        title = f.read()
    
    # 打印标题
    print(title)
    
    # 打印菜单
    # 打印动物列表
    print("请选择你想查看的动物：")
    for animal_id, info in animal_info.items():
        print(f"{animal_id}. 查看{info['name']}")
    # 打印退出选项
    print("q. 退出")

if __name__ == "__main__":
    display_title_menu()