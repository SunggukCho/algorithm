T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    dp = [0, 1, 3]
    num = N // 10
    if num > 2:
        for i in range(3, num+1):
            next = dp[i-1]+dp[i-2]*2
            dp.append(next)
    result = dp[-1]
    print('#{} {}'.format(tc, result))
