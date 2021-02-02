'''
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''
from collections import deque
def left(r, c, d):
    if d == 0:      #북쪽을 바라볼 때 왼쪽은 서쪽
        return 3
    elif d == 1:    #동쪽을 바라볼 때 왼쪽은 북쪽
        return 0
    elif d == 2:    #남쪽을 바라볼 때 왼쪽은 동쪽
        return 1
    elif d == 3:    #서쪽을 바라볼 때 왼쪽은 남쪽
        return 2


dr= [-1, 0, 1, 0]
dc= [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
cleaned = [[0]*M for _ in range(N)] #청소가 된 공간 표기

#현 위치 r, c
#방향 d [0:북, 1:동, 2:남, 3:서]

Q = deque()
Q.append([r, c])
while Q:
    x, y = Q.popleft()
    dir = d
    # 1. 현 위치 청소
    cleaned[x][y] = 1
    # 2. 왼쪽 탐색
    lft = left(x, y, dir)
    nx = x+dr[lft]
    ny = y+dc[lft]
    # 2-1. 만약 왼쪽이 청소할 수 있다면
    if MAP[nx][ny] != 1 and 0 <= nx < N and 0 <= ny < M:
        #해당 방향으로 회전 후 청소
        
    # 2-2. 만약 왼쪽이 청소할 수 없다면
        #해당 방향으로 회전 후 다시 왼쪽 탐색
        #4방향 다 막혀있다면 -> 후진

    # 3. 후진
        # 3-1. 후진 O
        # 3-2. 후진 X


