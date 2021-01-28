'''
풀이
DFS재귀 방식으로 돌면서 방문배열에 표시
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

'''
import copy
import sys; sys.setrecursionlimit(100000)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, visited):
    visited[r][c] = 1 #방문표시
    for k in range(4):
        nr = r+dr[k]
        nc = c+dc[k]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            dfs(nr, nc, visited)


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
G = [[0]*N for _ in range(N)] #방문배열

# 1. 마을 최고 높은 곳을 찾아라
maxH = 0    #마을에서 최고 높이
for i in range(N):
    if max(MAP[i]) > maxH:
        maxH = max(MAP[i])

maxV = 1    #안전한 영역의 최대 갯수
# 2. (마을 최고 높이-1)까지 한 칸 씩 수위를 높여본다.
for j in range(maxH):
    #j는 수위, j보다 낮은 곳은 방문처리
    for k in range(N):
        for l in range(N):
            if MAP[k][l] <= j:
                G[k][l] = 1
    #각 수위별로 그때 그때 구간 갯수를 cnt한다.
    cnt = 0
    visited = copy.deepcopy(G)
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                dfs(r, c, visited)
                cnt += 1
    if cnt > maxV:
        maxV = cnt
print(maxV)
