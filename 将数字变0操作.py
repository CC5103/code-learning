#给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。

def solution (n:int) -> int:
    dp = {}
    num = 0
    for i in range(n):
        if i == 0:
            dp[i] = n
            continue
        num += 1
        if dp[i - 1]%2 == 0:
            dp[i] = dp[i-1]/2
        else:
            dp[i] = dp[i-1]-1
        if dp[i] == 0:
            return num

print(solution(8))