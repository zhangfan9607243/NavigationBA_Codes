from config_test import *
from function_time_value import calculate_time_value

# 测试净现值计算功能的正确性
def test_calculate_time_value():

    test_cases = [
        # (1) 单笔现值按期复利增长
        (-1000.0, 1628.894627, 0.0, 0.05, 10),

        # (2) 期末等额存入（年金），初始 PV = 0
        (0.0, 12577.892536, -1000.0, 0.05, 10),

        # (3) 贷款：求得 PMT 使 FV = 0
        (10000.0, 0.0, -2637.974808, 0.10, 5),

        # (4) 零息：-950 投入 5 期变 1000
        (-950.0, 1000.0, 0.0, 0.010311, 5),

        # (5) 退休储蓄：期末缴款至目标 FV
        (0.0, 1500000.0, -15879.605267, 0.07, 30),

        # (6) 抵押贷款：月利 0.5%，10 年（120 期）摊还至 0
        (500000.0, 0.0, -5551.025097, 0.005, 120),

        # (7) 定期存款：单笔 -5000，2% 利率 10 期
        (-5000.0, 6094.972100, 0.0, 0.02, 10),

        # (8) 分期融资：6 期、每期 8%，摊还至 0
        (20000.0, 0.0, -4326.307725, 0.08, 6),

        # (9) 年金现值：给定 PMT 与 r、n，使 FV = 0
        (7721.734929, 0.0, -1000.0, 0.05, 10),

        # (10) 教育基金：期末缴款至目标 FV
        (0.0, 200000.0, -3645.343642, 0.06, 25),
    ]

    inputs_idx = ["PV", "FV", "PMT", "R", "N"]

    for idx, case in enumerate(test_cases):
        print("测试:", idx+1)
        case_list = list(case)

        for i in range(5):
            inputs = case_list.copy()
            inputs[i] = None  # 将第i个参数设为None，表示要求解该参数

            result = calculate_time_value(tuple(inputs))
            expected = case_list[i]

            # 使用近似比较，允许一定的误差范围
            assert abs(result[i] - expected) < 0.1, f"    求解参数{inputs_idx[i]}失败：期望{round(expected, 4)} & 得到{round(result[i], 4)}"
            print(f"    求解参数{inputs_idx[i]}成功：期望{round(expected, 4)} & 得到{round(result[i], 4)}")

    print("所有测试通过。")

if __name__ == "__main__":
    test_calculate_time_value()