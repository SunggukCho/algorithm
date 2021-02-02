'''
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
결국 구글링...
DFS인줄 알았는데 분류 보니까 DP였네...
아 씨 어제 DP유튜브 봤었는데 ㄲㅂ ㅠㅠ
'''
import sys; sys.setrecursionlimit(100000)

def dfs(r, c):
    if not G[r][c]:
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            #4방탐색 후 갈 수 있는 조건이라면 현재 위치에서보다 최소한 하루 더 살 수 있음
            if 0 <= nr < n and 0 <= nc < n and MAP[r][c] < MAP[nr][nc]:
                G[r][c] = max(dfs(nr, nc), G[r][c]) #현재까지 위치 vs 더 갈 수 있는 공간 중 더 큰 것 선택
        G[r][c] += 1    #max보다 하루 더 살 수 있으므로 +1해줌
    return G[r][c]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]
G = [[0]*n for _ in range(n)]

maxV = 0
for i in range(n):
    for j in range(n):
        maxV = max(dfs(i, j), maxV)
print(maxV)
