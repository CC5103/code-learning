# Problem: 爬楼梯最少成本
"""
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。

请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
"""
def solution (n:list) -> int:
    dp = [0]*(len(n) + 1)
    for num in range(len(n) + 1):
        if num == 0 or num == 1:
            dp[num] = 0
            continue
        dp[num] = min(dp[num-1]+n[num-1], dp[num-2]+n[num-2])
    return dp[len(n)]

print(solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))