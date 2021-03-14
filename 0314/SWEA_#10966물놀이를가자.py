'''
SWEA_#10966물놀이를 가자
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXMZta-PsDFAST

3
2 3
WLL
LLL
3 2
WL
LL
LW
4 5
LLLWW
WWLLL
LLLWL
LWLLL
'''
from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):
    Q = deque()
    Q.append((r, c, 0))
    while Q:
        r, c, cnt = Q.popleft()
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 'L':
                if visited[nr][nc] == -1:
                    visited[nr][nc] = cnt+1
                    Q.append((nr, nc, cnt+1))
                elif visited[nr][nc] > cnt:
                    visited[nr][nc] = min(cnt+1, visited[nr][nc])
                    Q.append((nr, nc, visited[nr][nc]))
    return visited

T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(M)]
    visited = [[-1] * N for _ in range(M)]
    waters = []
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 'W':
                waters.append((i, j))   #기존땅은 -1처리
                visited[i][j] = 0       #물있는곳은 0처리

    for water in waters:
        r, c = water
        bfs(r, c)
    ans = 0
    for row in visited:
        ans += sum(row)

    print('#{} {}'.format(tc, ans))
