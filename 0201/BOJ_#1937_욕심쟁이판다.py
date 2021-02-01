'''
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
'''
import sys; sys.setrecursionlimit(100000)

def dfs(r, c):
    if not G[r][c]:
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0 <= nr < n and 0 <= nc < n and MAP[r][c] < MAP[nr][nc]:
                G[r][c] = max(dfs(nr, nc), G[r][c])
        G[r][c] += 1
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
