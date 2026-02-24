from config_test import *
from function_expression import calculate_expression, expression_check, InvalidExpressionError

# 测试表达式计算功能的正确性
def test_calculate_expression():

    import math

    # 检查表达式计算结果是否正确的辅助函数
    def check_expression(expression, value):
        if math.fabs(calculate_expression(expression) - value) < 1e-10:
            return True
        else:
            return False

    # 测试基本的加减乘除运算、括号、正负号
    assert check_expression("2 + 3 * 4 - 5 / 2", 2 + 3 * 4 - 5 / 2)
    assert check_expression("((2 + 3) * 4) / 5", ((2 + 3) * 4) / 5)
    assert check_expression("(1 + 2) * (3 + 4)", (1 + 2) * (3 + 4))
    assert check_expression("-(1 + 2) * +(3 + 4)", -(1 + 2) * +(3 + 4))

    # 测试包含数学常数和函数的表达式
    # square(x)：平方函数
    assert check_expression("square(5)", 25)
    # pow(x, y)：x 的 y 次幂
    assert check_expression("pow(2, 3)", 8)
    # exp(x)：指数函数
    assert check_expression("exp(1)", math.e)
    # sqrt(x)：平方根
    assert check_expression("sqrt(16)", 4)
    # root(x, y)：x 的 y 次根
    assert check_expression("root(27, 3)", 3)
    # reciprocal(x)：取倒数
    assert check_expression("reciprocal(4)", 0.25)
    # ln(x)：自然对数
    assert check_expression("ln(e)", 1)
    # log2(x)：以 2 为底，x 的对数
    assert check_expression("log2(8)", 3)
    # log10(x)：以 10 为底，x 的对数
    assert check_expression("log10(100)", 2)
    # log(x, y)：以 y 为底，x 的对数
    assert check_expression("log(100, 10)", 2)
    # sin(x)：正弦函数
    assert check_expression("sin(0)", 0)
    assert check_expression("sin(pi/2)", 1)
    # cos(x)：余弦函数
    assert check_expression("cos(0)", 1)
    assert check_expression("cos(pi)", -1)
    # tan(x)：正切函数
    assert check_expression("tan(0)", 0)
    assert check_expression("tan(pi/4)", 1)
    # factorial(x)：阶乘函数
    assert check_expression("factorial(5)", 120)
    # abs(x)：绝对值函数
    assert check_expression("abs(-5)", 5)
    # C(n, k)：组合数函数，计算从 n 个元素中取 k 个元素的组合数
    assert check_expression("C(5, 2)", 10)
    # P(n, k)：排列数函数，计算从 n 个元素中取 k 个元素的排列数
    assert check_expression("P(5, 2)", 20)

    print("所有表达式计算测试通过！")


# 测试表达式合法性检查功能
def test_expression_check():

    # 检查表达式是否合法的辅助函数
    def check_expression(expression):
        try:
            expression_check(expression)
            return True
        except InvalidExpressionError:
            return False
    
    # 合法表达式
    assert check_expression("2 + 3 * 4 - 5 / 2") == True
    assert check_expression("square(5) + pow(2, 3)") == True
    assert check_expression("1 * 9 + -sin(pi / 2) + cos(0)") == True
    assert check_expression("C(5, 2) / P(5, 2)") == True
    assert check_expression("ln(e) + log10(100) - sqrt(16)") == True

    # 非法表达式
    assert check_expression("import os; os.system('rm -rf /')") == False
    assert check_expression("__import__('os').system('ls')") == False
    assert check_expression("open('file.txt', 'w')") == False
    assert check_expression("exec('print(123)')") == False
    assert check_expression("lambda x: x + 1") == False

    print("所有表达式合法性检查测试通过！")


if __name__ == "__main__":
    # test_calculate_expression()
    test_expression_check()
