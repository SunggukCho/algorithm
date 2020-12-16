"""
1
5
0 0 0 0 0
0 1 1 1 0
0 1 10 1 0
0 1 1 1 0
0 0 0 0 0
"""


def solve(k):
    global ans
    if k == len(food):
        tsum = 0
        for h in range(len(home)):
            tmin = 1e9
            for f in range(len(subset)):
                if subset[f]:
                    tmin = min(tmin, dist[f][h])
        for f in range(len(subset)):
            if subset[f]:
                tsum += food[f][2]
        if ans > tsum:
            ans = tsum
    else:
        subset[k] = 1
        solve(k + 1)
        subset[k] = 0
        solve(k + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 자료 매핑
    home, food = [], []
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                home.append((i,j))
            elif mat[i][j] > 1:
                food.append((i,j,mat[i][j]]))


    ans = 1e9
    subset = [0] * len(food)
    solve(0)
    dist = [[0]*len(home) for i in range(len(food))]
    for i in range(len(food)):
        for j in range(len(home)):
            dist[i][j] = abs(food[i][0] - home[j][0] + abs(food[i][j]) - home[j][1])

    print("#%d" % tc, ans)