from ui import show_instructions
from logger import log_write

# 计算表达式的函数
def calculate_expression(expression):

    # 定义数学常数和函数
    import math
    # pi
    pi = math.pi
    # e
    e = math.e
    # square(x)：平方函数
    def square(x):
        return x * x
    # pow(x, y)：x 的 y 次幂
    def pow(x, y):
        return x ** y
    # exp(x)：指数函数
    def exp(x):
        return math.e ** x
    # sqrt(x)：平方根
    def sqrt(x):
        return x ** 0.5
    # root(x, y)：x 的 y 次根
    def root(x, y):
        return x ** (1 / y)
    # reciprocal(x)：取倒数
    def reciprocal(x):
        return 1 / x
    # ln(x)：自然对数
    def ln(x):
        return math.log(x, math.e)
    # log2(x)：以 2 为底，x 的对数
    def log2(x):
        return math.log(x, 2)
    # log10(x)：以 10 为底，x 的对数
    def log10(x):
        return math.log(x, 10)
    # log(x, y)：以 y 为底，x 的对数
    def log(x, y):
        return math.log(x, y)
    # sin(x)：正弦函数
    def sin(x):
        return math.sin(x)
    # cos(x)：余弦函数
    def cos(x):
        return math.cos(x)
    # tan(x)：正切函数
    def tan(x):
        return math.tan(x)
    # factorial(x)：阶乘函数
    def factorial(x):
        return math.factorial(x)
    # abs(x)：绝对值函数
    def abs(x):
        return math.fabs(x)
    # C(n, k)：组合数函数，计算从 n 个元素中取 k 个元素的组合数
    def C(n, k):
        return math.comb(n, k)
    # P(n, k)：排列数函数，计算从 n 个元素中取 k 个元素的排列数
    def P(n, k):
        return math.perm(n, k)

    # 使用 eval 计算表达式
    result = eval(expression)
    return result

# 定义表达式非法类
class InvalidExpressionError(Exception):
    pass

# 表达式合法性检查函数
def expression_check(expression):

    # 定义允许的函数和常数列表
    valid_funcs = [
        "pi", "e",
        "square", "pow", "exp", "sqrt", "root", "reciprocal",
        "ln", "log2", "log10", "log", "sin", "cos", "tan",
        "factorial", "abs", "C", "P"]
    
    # 分割表达式，提取出所有的标识符
    expression_list = (expression.replace('(', ' ').
                                  replace(')', ' ').
                                  replace('+', ' ').
                                  replace('-', ' ').
                                  replace('*', ' ').
                                  replace('/', ' ').
                                  replace('%', ' ').
                                  replace('.', ' ').
                                  replace(',', ' ').
                                  split())

    # 检查表达式合法性
    is_valid = True
    for item in expression_list:
        if not item.isnumeric() and item not in valid_funcs:
            is_valid = False
    
    # 如果不合法，抛出异常，否则返回表达式
    if not is_valid:
        raise InvalidExpressionError("表达式包含不合法的标识符！")
    else:
        return expression

# 表达式计算功能主函数
def function_expression_main():

    while True:

        # 展示功能菜单
        print("-" * 40)
        print("表达式计算功能：")
        print("0. 查看功能说明")
        print("1. 计算表达式")
        print("q. 返回主菜单")
        print("-" * 40)
        
        # 获取用户选择
        choice = input("请选择功能（0/1/q）：")
        print("-" * 40)
        
        # 0. 查看功能说明
        if choice == "0":
            show_instructions(function_key="1")
            print("-" * 40)
        
        # 1. 计算表达式
        elif choice == "1":

            while True:
                
                # 获取用户输入的表达式
                expression = input("请输入数学表达式（输入 'exit' 退出）：").strip()
                
                # 退出
                if expression == "exit":
                    break
                
                # 计算表达式
                try:
                    # 检查并计算表达式
                    expression_checked = expression_check(expression)
                    result = round(calculate_expression(expression_checked), 4)
                    # 输出计算结果
                    print("计算结果：", result)
                    # 记录计算历史日志
                    log_write("计算历史", {
                        "功能": "算式计算",
                        "输入": expression_checked,
                        "结果": result
                    })
                    # 询问是否继续计算
                    print("-" * 40)
                    choice_continue = input("是否继续计算？(y/n)：").strip().lower()
                    print("-" * 40)
                    if choice_continue != "y":
                        break
                
                # 处理计算错误
                except InvalidExpressionError as e1:
                    print("表达式非法：", e1, "请检查后重新输入表达式。")
                    log_write("计算历史", {
                        "功能": "算式计算",
                        "输入": expression,
                        "结果": "程序错误：" + str(e1)
                    })
                    print("-" * 40)
                except Exception as e2:
                    print("表达式错误：", e2, "请检查后重新输入表达式。")
                    log_write("计算历史", {
                        "功能": "算式计算",
                        "输入": expression,
                        "结果": "程序错误：" + str(e2)
                    })
                    print("-" * 40)
        
        # q. 返回主菜单
        elif choice == "q":
            break
        
        # 其他. 无效输入
        else:
            print("无效输入，请重新选择。")

if __name__ == "__main__":
    function_expression_main()