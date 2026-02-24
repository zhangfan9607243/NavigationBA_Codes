from datetime import datetime
from config import PATH_PREFIX

def logger(message):
    # 日志文件路径
    log_file_path = PATH_PREFIX + "logs/zoo.log"

    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 定义日志信息
    log_content = f"时间：{current_time}\n消息：{message}\n\n"

    # 写入日志
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(log_content)

if __name__ == "__main__":
    logger("开发者测试日志记录功能")