from ui import show_instructions
from logger import log_write
import numpy_financial as npf
import numpy as np

def get_cash_flow_list():
    while True:
        print("-" * 40)
        print("请输入现金流列表（以逗号分隔的数字，例如 -1000, 300, 400）：")
        cash_flow_str = input("请输入现金流列表：")
        try:
            cash_flow_list = [float(cash.strip()) for cash in cash_flow_str.split(',')]
            print("现金流列表输入成功：", cash_flow_list)
            print("-" * 40)
            return cash_flow_list
        except ValueError:
            print("输入格式错误，请重新输入合法的现金流列表。")

def calculate_irr(cashflows):
    # 求所有根（x=1+r）
    roots = np.roots(cashflows)

    # 只保留实数根的实部
    roots_filtered = [r.real for r in roots if abs(r.imag) < 1e-8]

    # 转换为 irr，且只保留大于 -1 的解
    irr_values = [float(r) - 1 for r in roots_filtered if r - 1 > -1]

    # 如果没有实数根，返回 None
    if not irr_values:
        return [None]
    # 如果有实数根，则按从小到大排序返回
    else:
        return sorted(irr_values)

def calculate_npv(cash_flows, discount_rate):
    npv = 0.0
    for t, cf_t in enumerate(cash_flows):
        npv_t = cf_t / ((1 + discount_rate) ** t)
        npv += npv_t
    return npv

def get_discount_rate():
    while True:
        discount_rate_input = input("请输入折现率（小数形式，如 0.05 表示 5%）：").strip()
        try:
            discount_rate = float(discount_rate_input)
            return discount_rate
        except Exception:
            print("折现率格式错误，请输入数字！")

def function_cash_flow_main():
    
    while True:

        # 展示功能菜单
        print("-" * 40)
        print("现金流计算功能：")
        print("0. 使用说明")
        print("1. 输入现金流并进行运算")
        print("q. 返回主菜单")
        print("-" * 40)

        # 获取用户选择
        choice = input("请选择功能（0/1/q）：")
        print("-" * 40)

        # 0. 查看功能说明
        if choice == "0":
            show_instructions(function_key="2")
            print("-" * 40)
        
        # 1. 现金流计算
        elif choice == "1":
            
            while True:
                
                # 获取用户输入的现金流
                cash_flow_list = get_cash_flow_list()
                
                try:
                    # 计算IRR
                    irr = calculate_irr(cash_flow_list)
                    print("该现金流的内部收益率（IRR）为：", irr)  # 由于 IRR 被我们改成了列表，这里取消 round

                    # 计算NPV
                    discount_rate = get_discount_rate()
                    npv = calculate_npv(cash_flow_list, discount_rate=discount_rate)

                    # 输出计算结果
                    print("该现金流的净现值（NPV）为：", round(npv, 4))
                    
                    # 记录计算历史日志
                    log_write("计算历史", {
                        "功能": "现金流计算",
                        "现金流列表": cash_flow_list,
                        "IRR": irr,  # 由于 IRR 被我们改成了列表，这里取消 round
                        "折现率": discount_rate,
                        "NPV": round(npv, 4)
                    })
                    
                    # 询问是否继续计算
                    print("-" * 40)
                    choice_continue = input("是否继续计算？(y/n)：").strip().lower()
                    print("-" * 40)
                    if choice_continue != "y":
                        break
                
                # 计算过程中出现错误
                except Exception as err:
                    print("计算过程中出现错误：", err)
                    print("请重新输入现金流进行计算。")
                    log_write("计算历史", {
                        "功能": "现金流计算",
                        "现金流列表": cash_flow_list,
                        "结果": "程序错误：" + str(err)
                    })
                    print("-" * 40)
            
        # q. 返回主菜单
        elif choice == "q":
            break
        
        # 其他. 无效输入
        else:
            print("无效输入，请重新选择。")

if __name__ == "__main__":
    function_cash_flow_main()