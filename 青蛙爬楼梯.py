"""
今天的有氧运动训练内容是在一个长条形的平台上跳跃。平台有 num 个小格子，每次可以选择跳 一个格子 或者 两个格子。请返回在训练过程中，学员们共有多少种不同的跳跃方式。

结果可能过大，因此结果需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 5
输出：8
"""

def trainWays(n: int) -> int:
    memo = {}
    mod = 1e9  + 7
    for i in range(n+1):
        if i == 0 or i == 1:
            memo[i] = 1
            continue
        memo[i] = (memo[i - 1] + memo[i - 2]) % mod
    return(memo[n])

print(trainWays(5))