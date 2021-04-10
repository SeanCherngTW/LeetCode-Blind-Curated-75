from typing import List


def knapsack(weights: List, values: List, max_weight: int) -> int:
    """
    weights: weight of each items
    values: values of each items
    max_weight: max weight to take
    """
    res = 0
    num_items = len(weights)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(num_items)]
    for i in range(num_items):
        weight = weights[i]
        value = values[i]
        for j in range(1, max_weight + 1):
            if j - weight >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:
                dp[i][j] = dp[i - 1][j]

            res = max(dp[i][j], res)
    print(dp)


weights = [1, 4, 3]
values = [1500, 3000, 2000]
max_weight = 4

print(knapsack(weights, values, max_weight))
