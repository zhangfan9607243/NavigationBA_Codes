from config import PATH_PREFIX

animal_info ={
    "1": {
        "name": "骆驼", 
        "file": "data/animal1_camel.txt"
        },
    "2": {
        "name": "牛", 
        "file": "data/animal2_cow.txt"
        },
    "3": {
        "name": "马", 
        "file": "data/animal3_horse.txt"
    },
}

def display_animal(animal_id):    
    # 获取对应的文件路径
    file_path = PATH_PREFIX + animal_info[animal_id]["file"]

    # 读取动物ASCII艺术字
    with open(file_path, "r", encoding="utf-8") as f:
        animal_ascii = f.read()
    
    # 展示动物
    print(f"请看，这是一头{animal_info[animal_id]['name']}：")
    print(animal_ascii)
    input("输入任意内容退回到菜单")

if __name__ == "__main__":
    display_animal("1")