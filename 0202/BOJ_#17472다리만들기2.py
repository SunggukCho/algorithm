# BOJ #17472 다리만들기2
'''
7 8
0 0 0 0 0 0 1 1
1 1 0 0 0 0 1 1
1 1 0 0 0 0 0 0
1 1 0 0 0 1 1 0
0 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
풀이 순서
#1. 각각의 섬 별로 넘버링하기
#2. 길 연결하기
#3. 최소값 찾기
'''
from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c, land_num):
    Q = deque()
    Q.append([r, c])
    while Q:
        x, y = Q.popleft()
        MAP[x][y] = land_num
        G[x][y] = 1
        for k in range(4):
            nr = x+dr[k]
            nc = y+dc[k]
            if 0 <= nr < N and 0 <= nc < M and G[nr][nc] == 0:
                if MAP[nr][nc]:
                    MAP[nr][nc] = land_num
                    Q.append([nr, nc])


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
G = [[0]*M for _ in range(N)]

#1. 섬 넘버링
land_num = 1   #섬 no.1부터 시작
land_cnt = 0    #섬의 갯수
for i in range(N):
    for j in range(M):
        if MAP[i][j] and G[i][j] == 0:
            bfs(i, j, land_num)
            land_num += 1

#2.섬 연결

