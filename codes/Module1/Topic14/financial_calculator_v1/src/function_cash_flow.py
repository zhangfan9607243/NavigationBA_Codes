from ui import show_instructions
from logger import log_write
import numpy_financial as npf
import numpy as np

def get_cash_flow_list():

    # 获取用户输入的现金流
    cash_flows_tuples = []
    print("-" * 40)
    
    while True:
        # 获取现金流时间点
        cf_time = input("请输入现金流时间点（非负整数）：").strip()
        try:
            cf_time_int = int(cf_time)
            if cf_time_int < 0:
                print("时间点必须是非负整数，请重新输入！")
                continue
        except Exception:
            print("时间点格式错误，请输入非负整数！")
            continue
        # 获取现金流金额
        cf_value = input("请输入现金流金额：").strip()
        try:
            cf_value_float = float(cf_value)
        except Exception:
            print("现金流金额格式错误，请输入数字！")
            continue
        # 添加现金流到列表
        cash_flows_tuples.append((cf_time_int, cf_value_float))
        print("现金流已添加：时间点 =", cf_time_int, "金额 =", cf_value_float)
        print("-" * 40)
        # 询问是否继续添加现金流
        if input("是否继续添加现金流？(y/n)：").strip().lower() != "y":
            break
    
    # 按时间点排序现金流
    cash_flows_tuples.sort(key=lambda x: x[0])
    cash_flow_time_max = cash_flows_tuples[-1][0]

    # 构建完整的现金流列表
    cash_flows = [0.0] * (cash_flow_time_max + 1)
    for t, v in cash_flows_tuples:
        cash_flows[t] = v
    
    print("-" * 40)
    print("完整现金流列表已生成：", cash_flows)

    return cash_flows


def calculate_irr(cash_flows):
    try:
        irr = npf.irr(cash_flows)
        if irr is np.nan:
            return [None]
        else:
            return [float(irr)]
    except:
        return [None]

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