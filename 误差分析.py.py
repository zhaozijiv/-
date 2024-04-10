import math
import numpy as np

def calculate_uncertainty():
    # 获取用户输入的数据，自动将中文逗号替换为英文逗号
    measurements_input = input("请输入测量值，用逗号分隔: ").replace("，", ",")
    instrument_precision_half = float(input("请输入仪器最小分度值的一半: "))
    k_value_input = input("请输入k值: ")
    
    # 安全地评估k值表达式
    try:
        # 只允许数字和算术运算符，以及限定的数学函数
        k_value = eval(k_value_input, {"__builtins__": None}, {"sqrt": math.sqrt})
    except Exception as e:
        print(f"处理k值表达式时出错: {e}")
        print("使用默认值 1")
        k_value = 1
    
    # 将测量值字符串转换为数字列表
    measurements = np.array([float(x.strip()) for x in measurements_input.split(',')])
    
    # 计算平均值
    average = np.mean(measurements)
    
    # A类不确定度（随机误差）
    Ua = np.sqrt(np.sum((measurements - average) ** 2) / (len(measurements) * (len(measurements) - 1)))
    
    # B类不确定度（系统误差）
    Ub = instrument_precision_half / k_value
    
    # 合成不确定度
    Uc = np.sqrt(Ua**2 + Ub**2)
    
    # 相对不确定度
    relative_uncertainty = (Uc / average) * 100
    
    # 使用格式化字符串来保留五位小数
    print(f"平均值: {average:.5f} ± {Uc:.5f}")
    print(f"A类不确定度 (Ua): {Ua:.5f}")
    print(f"B类不确定度 (Ub): {Ub:.5f}")
    print(f"合成不确定度 (Uc): {Uc:.5f}")
    print(f"相对不确定度 (%): {relative_uncertainty:.5f}")

calculate_uncertainty()
