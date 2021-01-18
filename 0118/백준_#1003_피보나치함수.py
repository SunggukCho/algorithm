dp = [j for j in range(40 + 1)]
for i in range(2, 40 + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        M, N = 1, 0
    else:
        M, N = dp[n-1], dp[n]
    print(M, N)

