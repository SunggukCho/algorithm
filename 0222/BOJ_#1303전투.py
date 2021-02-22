'''
BOJ_#1303전투
https://www.acmicpc.net/problem/1303

5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW

답 130 65
'''
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def find(r, c, color):
    group = 0
    Q = deque()
    Q.append([r, c])
    visited[r][c] = 1
    while len(Q):
        x, y = Q.popleft()
        group += 1
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < M and 0 <= ny < N and MAP[nx][ny] == color:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    Q.append([nx, ny])
    return group


N, M = map(int, input().split())
#N - Column, M - Row
MAP = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

white = 0
blue = 0
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            ans = find(i, j, MAP[i][j])
            if MAP[i][j] == 'W':
                white += ans ** 2
            else:
                blue += ans ** 2

print('{} {}'.format(white, blue))
