import math

def calculate_combinations(n, k):
    combinations = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return int(combinations)

# 使用示例
total_combinations = calculate_combinations(32, 5)
print("总共的组合数量：", total_combinations)
