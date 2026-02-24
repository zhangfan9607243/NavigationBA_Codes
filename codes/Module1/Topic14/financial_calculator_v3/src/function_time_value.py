from ui import show_instructions
from logger import log_write
import math
import numpy_financial as npf
from user_settings import get_decimal_places, get_money_symbol
from utils import format_money

def get_time_value_inputs():
    while True:
        print("-" * 40)
        print("请输入金钱时间价值的参数：")
        print("格式为：PV, FV, PMT, R, N，需要求的参数请输入 None")
        print("例如：-1000, None, -60, 0.05, 12")
        params_str = input("请输入参数：")
        try:
            params_list = []
            for param in params_str.split(','):
                param = param.strip()
                if param == 'None':
                    params_list.append(None)
                else:
                    params_list.append(float(param))
            if len(params_list) != 5:
                print("输入参数数量错误，请输入5个参数。")
                continue
            if params_list.count(None) != 1:
                print("请输入且仅输入一个参数为 None。")
                continue
            if params_list[3] is not None and not (params_list[3] > -1):
                print("折现率 R 必须大于-1。")
                continue
            if params_list[4] is not None and not (params_list[4] > 0):
                print("期数 N 必须是正数。")
                continue
            param_list_formatted = params_list.copy()
            param_list_formatted[0] = format_money(get_money_symbol(), get_decimal_places(), params_list[0]) if params_list[0] is not None else None
            param_list_formatted[1] = format_money(get_money_symbol(), get_decimal_places(), params_list[1]) if params_list[1] is not None else None
            param_list_formatted[2] = format_money(get_money_symbol(), get_decimal_places(), params_list[2]) if params_list[2] is not None else None
            param_list_formatted[3] = round(params_list[3], get_decimal_places()) if params_list[3] is not None else None
            param_list_formatted[4] = round(params_list[4], get_decimal_places()) if params_list[4] is not None else None
            print("金钱时间价值参数输入成功：", param_list_formatted)
            print("-" * 40)
            return tuple(params_list), tuple(param_list_formatted)
        except ValueError:
            print("输入格式错误，请重新输入合法的参数列表。")


def calculate_time_value(tv_inputs):
    pv, fv, pmt, r, n = tv_inputs

    # 求解 PV
    if pv is None:
        pv = - (pmt * ((1 + r) ** n - 1) / r + fv) / (1 + r) ** n
    
    # 求解 FV
    elif fv is None:
        fv = - pv * (1 + r) ** n - pmt * ((1 + r) ** n - 1) / r
    
    # 求解 PMT
    elif pmt is None:
        pmt = - r * (pv * (1 + r) ** n + fv) / ((1 + r) ** n - 1)
    
    # 求解 N
    elif n is None:
        # n = npf.nper(pv=pv, fv=fv, pmt=pmt, rate=r)
        n = math.log((pmt - r * fv) / (pmt + r * pv)) / math.log(1 + r)
    
    # 求解 R
    else:
        # 直接调用 numpy_financial 包中的 rate 函数
        r = npf.rate(pv=pv, fv=fv, pmt=pmt, nper=n)

    # 格式化输出结果
    result_tuple = (pv, fv, pmt, r, n)
    result_tuple_formatted = (
        format_money(get_money_symbol(), get_decimal_places(), pv),
        format_money(get_money_symbol(), get_decimal_places(), fv),
        format_money(get_money_symbol(), get_decimal_places(), pmt),
        round(r, get_decimal_places()),
        round(n, get_decimal_places())
    )
    return result_tuple, result_tuple_formatted

# 金钱时间价值计算的函数
def function_time_value_main():
    
    while True:

        # 展示功能菜单
        print("-" * 40)
        print("金钱时间价值计算功能：")
        print("0. 查看功能说明")
        print("1. 计算金钱时间价值")
        print("q. 返回主菜单")
        print("-" * 40)
        
        # 获取用户选择
        choice = input("请选择功能（0/1/q）：")
        print("-" * 40)
        
        # 0. 查看功能说明
        if choice == "0":
            show_instructions(function_key="3")
            print("-" * 40)
        
        # 1. 计算金钱时间价值
        elif choice == "1":
            tv_inputs, tv_inputs_formatted = get_time_value_inputs()
            tv_result, tv_result_formatted = calculate_time_value(tv_inputs)

            print("参数输入为：")
            print("PV：", tv_inputs_formatted[0])
            print("FV：", tv_inputs_formatted[1])
            print("PMT：", tv_inputs_formatted[2])
            print("R：", tv_inputs_formatted[3])
            print("N：", tv_inputs_formatted[4])
            print("*" * 40)

            print("计算结果为：")
            print("PV：", tv_result_formatted[0])
            print("FV：", tv_result_formatted[1])
            print("PMT：", tv_result_formatted[2])
            print("R：", tv_result_formatted[3])
            print("N：", tv_result_formatted[4])
            print("*" * 40)

            input("输入任意内容返回主菜单：")

            log_write("计算历史", {
                "功能": "时间价值计算",
                "输入参数": tv_inputs_formatted,
                "结果": tv_result_formatted
                }
            )

            print("-" * 40)
        
        # q. 返回主菜单
        elif choice.lower() == "q":
            break
        
        # 非法输入处理
        else:
            print("输入不合法，请重新选择！")
            print("-" * 40) 

if __name__ == "__main__":
    function_time_value_main()