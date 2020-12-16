"""
1
10 40 100 300
0 0 2 9 1 5 0 0 0 0 0 0
"""
def dfs(n, s):
    global result
    if n >= 12:
        if s < result:
            result = s
    else:
        dfs(n+1, s+day*plan[n])
        dfs(n+1, s+month)
        dfs(n+3, s+tmonth)

T = int(input())
for tc in range(1, T+1):
    day, month, tmonth, year = map(int, input().split())
    plan = list(map(int, input().split()))

    result = year
    dfs(0,0)
    print('#{} {}'.format(tc, result))
