# https://atcoder.jp/contests/abc267/tasks/abc267_c

N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_A = sum([(i)*a for i,a in enumerate(A[:M], start=1)])
sum_B = sum(A[0:M])
best = sum_A

for j in range(1,N-M+1):
    sum_A = sum_A -sum_B + M*A[j+M-1]
    sum_B = sum_B - A[j-1] + A[j+M-1]
    if best < sum_A:
        best = sum_A
print(best)