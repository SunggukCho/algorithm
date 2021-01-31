N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# dp[i]는 i번째날까지 일을 했을 때, 최대값이다.
dp = [0 for i in range(N+1)]

for i in range(len(T)-1, -1, -1):    #역순으로 진행
    if T[i]+i <= N:
        dp[i] = max(P[i]+dp[i+T[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])
