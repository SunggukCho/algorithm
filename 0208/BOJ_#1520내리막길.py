'''
4 5  
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''
import sys
sys.setrecursionlimit(1000000)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    # global visited
    if r == M-1 and c == N-1:    #도착
        # print(r, c)
        return 1
    if visited[r][c]:   #이전에 방문했었다면
        # print(r, c)
        return visited[r][c]

    #첫방문이라면 일단 넘어감
    for k in range(4):
        # print(r, c)
        nr = r+dr[k]
        nc = c+dc[k]
        if 0 <= nr < M and 0 <= nc < N:
            if MAP[r][c] > MAP[nr][nc]:
                visited[r][c] += dfs(nr, nc)
    return visited[r][c]


M, N = map(int, input().split())    #M세로(행row), N가로(열col)
MAP = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)] #방문배열

ans = dfs(0, 0)
print(ans)
#print(visited)
# print(visited[0][0])

