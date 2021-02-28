'''
BOJ_#1726로봇
https://www.acmicpc.net/problem/1726
BFS방식으로 방문배열에 Cnt를 찍어가면서 Cnt최소값으로 갱신해주고 마지막에 end지점의 visited를 출력하면 될 것 같음
-> Queue 방식을 써보자
...
흠... 거의 다 온 거 같은데 너무 피곤함...ㅠ

'''
from collections import deque
dr = [0, 0, 1, -1]  #동서남북
dc = [1, -1, 0, 0]

def turn_r(x, y, dir, cnt):
    if dir == 0: ndir = 2
    elif dir == 1: ndir = 3
    elif dir == 2: ndir = 1
    else: ndir = 0
    if visited[x][y][ndir] == 0:
        visited[x][y][ndir] = visited[x][y][dir] + 1
        Q.append([x, y, ndir, cnt])

def turn_l(x, y, dir, cnt):
    if dir == 0: ndir = 3
    elif dir == 1: ndir = 2
    elif dir == 2: ndir = 0
    else: ndir = 1
    if visited[x][y][ndir] == 0:
        visited[x][y][ndir] = visited[x][y][dir] + 1
        Q.append([x, y, ndir, cnt])


M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(M)]
start_r, start_c, start_dir = map(int, input().split())
end_r, end_c, end_dir = map(int, input().split())

visited = [[[0]*5 for _ in range(N)] for _ in range(M)]
Q = deque()
global_cnt = 0
Q.append((start_r-1, start_c-1, start_dir, global_cnt))
ans = 0
while len(Q):
    r, c, d, cnt = Q.popleft()
    if r == end_r - 1 and c == end_c - 1 and d == end_dir-1:  #도착
        ans = cnt
        for row in visited:
            print(row)
        break
    #좌/우 회전 체크
    turn_l(r, c, d, cnt)
    turn_r(r, c, d, cnt)

    for k in range(3):  #최대 3칸까지 전진 가능
        nr = r+dr[d]*k
        nc = c+dc[d]*k
        if 0 <= nr < M and 0 <= nc < N and MAP[nr][nc] == 0:# 전진 가능
            if visited[nr][nc][d] == 0:
                visited[nr][nc][d] = cnt+1
                Q.append((nr, nc, d, cnt+1))
        else:  #전진 실패
            turn_l(r, c, d, cnt)
            turn_r(r, c, d, cnt)
print(ans)

