import json
from datetime import datetime
from config import PATH_PREFIX

LOG_FILE = f"{PATH_PREFIX}log/fc.log"


def log_write(log_type, content):

    # 生成日志条目的字典
    log_entry = {
        "时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "类型": log_type,
        "内容": content
    }
    
    # 以追加模式写入日志文件
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")


def log_read(log_type="计算历史", page_size=5):

    # 读取日志文件内容
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.readlines()

    # 将符合类型的日志解析后储存为一个列表
    logs_json = [json.loads(log) for log in logs if json.loads(log)["类型"] == log_type]

    # 计算需要分多少页显示
    n_logs = len(logs_json)
    n_pages = (n_logs + page_size - 1) // page_size

    # 分页显示日志内容
    for page in range(n_pages):

        # 计算当前页的起始和结束索引
        si = page * page_size
        ei = min(si + page_size, n_logs)
        
        # 循环显示当前页日志
        print("=" * 40)
        print(f"第 {page + 1} 页，共 {n_pages} 页")
        
        for log in logs_json[si:ei]:
            print("-" * 40)
            print(json.dumps(log, ensure_ascii=False, indent=4))
        
        # 询问用户是否继续查看下一页
        if page < n_pages - 1:
            print("-" * 40)
            cont = input("是否继续查看下一页？(y/n): ")
            # 如果用户输入不是 'y'，则退出查看
            if cont.lower() != 'y':
                print("退出查看日志")
                print("=" * 40)
                break
    
    # 如果已经显示完所有页，正常退出
    else:
        print("-" * 40)
        print("已显示所有日志记录，退出查看日志")
        print("=" * 40)


if __name__ == "__main__":
    # log_write("开发者测试-系统日志", "开发者测试系统日志")
    # log_write("开发者测试-计算历史", {
    #     "功能": "算式计算",
    #     "输入": "2 + 3 * 4",
    #     "结果": 14
    # })
    # log_write("开发者测试-计算历史", {
    #     "功能": "现金流计算",
    #     "现金流列表": [-1000, 300, 400, 500, 600],
    #     "计算对象": "NPV",
    #     "折现率": 0.1,
    #     "结果": 388.77
    # })
    # log_write("开发者测试-计算历史", {
    #     "功能": "时间价值计算",
    #     "输入参数": {
    #         "PV": 1000,
    #         "FV": None,
    #         "R": 0.05,
    #         "PMT": 100,
    #         "n": 10
    #     },
    #     "结果": 2886.68
    # })
    log_read("开发者测试-计算历史")