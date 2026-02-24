from config_test import *
from function_cash_flow import calculate_npv, calculate_irr

# 测试净现值计算功能的正确性
def test_calculate_irr_npv():

    def test_irr(cash_flows):
        
        irr_list = calculate_irr(cash_flows)
        irr_valid_list = [False for irr in irr_list]
        
        if irr_list == [None]:
            # 直接在这里判断现金流是否发生过变号（忽略 0）
            signs = [cf > 0 for cf in cash_flows if cf != 0]

            # 若列表非空且存在相邻符号不同，则说明发生变号
            if signs and any(sign != signs[0] for sign in signs):
                return [False] # 有变号（理论上可能有IRR）
            else:
                return [True]  # 无变号（理论上无IRR）

        else:
            for idx, irr in enumerate(irr_list):
                npv = calculate_npv(cash_flows, irr)
                if abs(npv) < 0.01:
                    irr_valid_list[idx] = True
                else:
                    irr_valid_list[idx] = False
        
        if all(irr_valid_list):
            return True
        else:
            return False

    def test_npv(cash_flows, discount_rate, npv_expected):
        npv_calculated = calculate_npv(cash_flows, discount_rate)
        if abs(npv_calculated - npv_expected) < 0.01:
            return True
        else:
            return False


    # 测试用例：格式为：(现金流列表, 折现率, NPV)
    test_cases = [
        ([-1000, 200, 300, 400, 500, 600], 0.08, 535.7846),
        ([-5000, -2000, 3000, 4000, 5000, 6000], 0.10, 5807.0114),
        ([-10000, 0, 0, 0, 0, 25000], 0.12, 4185.6714),
        ([-8000, -2000, 4000, 5000, 6000, 7000], 0.09, 6192.8460),
        ([-3000, 800, 800, 800, 800, 800], 0.06, 369.8910),
        ([-10000, 5000, -2000, 7000, 3000, 4000], 0.11, 2349.5975),
        ([10000, -3000, -3000, -3000, -3000], 0.07, -161.6338),
        ([-2000, 600, 600, 600, 600], 0.05, 127.5703),
        ([-15000, -5000, 4000, 6000, 8000, 10000], 0.13, -1799.7419),
        ([-5000, -1000, -500, 0, 8000, 9000], 0.15, 2800.9795),
    ]

    for cash_flows, discount_rate, expected_npv in test_cases:
        assert test_irr(cash_flows)
        assert test_npv(cash_flows, discount_rate, expected_npv)

    print("所有 IRR 和 NPV 测试通过！")

if __name__ == "__main__":
    test_calculate_irr_npv()
