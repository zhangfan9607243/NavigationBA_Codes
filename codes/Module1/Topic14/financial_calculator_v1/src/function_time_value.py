from ui import show_instructions
from logger import log_write
import math
import numpy_financial as npf

def get_time_value_inputs():
    # 外层循环，确保用户输入正确
    while True:
        # PV
        print("*" * 40)
        print("请输入以下金钱时间价值计算所需的参数：")
        while True:
            try:
                pv_input = input("请输入PV（输入None表示要求现值）：").strip()
                if pv_input.lower() == "none":
                    pv = None
                else:
                    pv = float(pv_input)
                break
            except Exception:
                print("PV格式错误，请输入数字或None。")
        print("PV输入完成：", pv)
        # FV
        print("*" * 40)
        while True:
            try:
                fv_input = input("请输入FV（输入None表示要求终值）：").strip()
                if fv_input.lower() == "none":
                    fv = None
                else:
                    fv = float(fv_input)
                break
            except Exception:
                print("FV格式错误，请输入数字或None。")
        print("FV输入完成：", fv)
        # PMT
        print("*" * 40)
        while True:
            try:
                pmt_input = input("请输入PMT（输入None表示要求每期支付金额）：").strip()
                if pmt_input.lower() == "none":
                    pmt = None
                else:
                    pmt = float(pmt_input)
                break
            except Exception:
                print("PMT格式错误，请输入数字或None。")
        print("PMT输入完成：", pmt)
        # R
        print("*" * 40)
        while True:
            try:
                r_input = input("请输入R（输入None表示要求利率）：").strip()
                if r_input.lower() == "none":
                    r = None
                else:
                    r = float(r_input)
                if r is not None and r <= -1:
                    print("R不能小于或等于 -1，请重新输入。")
                    continue
                break
            except Exception:
                print("R格式错误，请输入数字或None。")
        print("R输入完成：", r)
        # N
        print("*" * 40)
        while True:
            try:
                n_input = input("请输入N（输入None表示要求期数）：").strip()
                if n_input.lower() == "none":
                    n = None
                else:
                    n = int(n_input)
                if n is not None and n < 0:
                    print("N不能为负数，请重新输入。")
                    continue
                break
            except Exception:
                print("N格式错误，请输入整数或None。")
        print("N输入完成：", n)
        # 汇总结果
        print("*" * 40)
        tv_inputs = (pv, fv, pmt, r, n)
        if tv_inputs.count(None) != 1:
            print("输入错误：必须且只能有一个参数为None，请重新输入所有参数。")
            print("*" * 40)
            continue
        else:
            print("所有参数输入完成。")
            print("*" * 40)
            break
    # 返回结果  
    return tv_inputs


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

    return (pv, fv, pmt, r, n)

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
            tv_inputs = get_time_value_inputs()
            tv_result = calculate_time_value(tv_inputs)

            print("参数输入为：")
            print("PV：", tv_inputs[0])
            print("FV：", tv_inputs[1])
            print("PMT：", tv_inputs[2])
            print("R：", tv_inputs[3])
            print("N：", tv_inputs[4])
            print("*" * 40)

            print("计算结果为：")
            print("PV：", tv_result[0])
            print("FV：", tv_result[1])
            print("PMT：", tv_result[2])
            print("R：", tv_result[3])
            print("N：", tv_result[4])
            print("*" * 40)

            input("输入任意内容返回主菜单：")

            log_write("计算历史", {
                "功能": "时间价值计算",
                "输入参数": tv_inputs,
                "结果": tv_result
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