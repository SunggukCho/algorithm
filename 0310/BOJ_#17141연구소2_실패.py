'''
BOJ_#17141 연구소2
https://www.acmicpc.net/problem/17141
BFS로 visited를 채운다.
경우의 수를 구하고 각 경우의 수 마다 BFS를 돌린다.
이때 모두 퍼져있는지 체크하고 (1), visited 값이 최소인 것을 갱신(2)한다.

'''
from itertools import combinations
from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def bfs(r, c):
    visited[r][c] = 0
    Q = deque()
    Q.append((r, c, 0))
    while Q:
        r, c, cnt = Q.popleft()
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0 <= nr < N and 0 <= nc < N and lab[nr][nc] != 1:
                if visited[nr][nc] > cnt:
                    Q.append((nr, nc, cnt+1))
                    visited[nr][nc] = cnt + 1
                elif visited[nr][nc] == -1:
                    Q.append((nr, nc, cnt + 1))
                    visited[nr][nc] = visited[r][c]+1


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus = deque()
walls = deque()
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:      #바이러스 투척 장소
            virus.append((i, j))
        elif lab[i][j] == 1:    #벽
            walls.append((i, j))

virus_combs = list(combinations(virus, M))
result = -1
for combs in virus_combs:
    visited = [[-1]*N for _ in range(N)]    #첫 출발을 0으로 둬야 하기 때문에 -1로 둔다.

    for x, y in walls:
        visited[x][y] = 0

    for comb in combs:
        r, c = comb
        bfs(r, c)

    flag = True #전부 다 퍼져있는가?
    maxV = 0
    for i in visited:
        min_row = min(i)
        if min_row == -1:
            flag = False
            break
        else:
            max_row = max(i)
            maxV = max(max_row, maxV)

    if flag:
        if result > maxV or result == -1:
            result = maxV

print(result)
