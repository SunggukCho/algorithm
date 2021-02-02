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
def back(r, c, d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 0:
        return 1
    elif d == 3:
        return 1


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
cleaned = [[0]*M for _ in range(N)] #청소가 된 공간 표기

#현 위치 r, c
#방향 d [0:북, 1:동, 2:남, 3:서]

Q = deque()
Q.append([r, c])
cleaned[r][c] = 1
while Q:
    x, y = Q.popleft()
    # 1. 현 위치 4방 탐색
    for k in range(4):
        dir = (d-1) % 4 #왼쪽부터
        nx = x+dr[dir]
        ny = y+dc[dir]
        # 2. 만약 왼쪽이 청소할 수 있다면
        if MAP[nx][ny] != 1 and 0 <= nx < N and 0 <= ny < M:
            if cleaned[nx][ny] == 0:
            # 아직 청소가 안되어있다면, 해당 방향으로 회전 후 청소
                cleaned[nx][ny] = 1
                Q.append([nx, ny])
                break
    #여기까지 왔다는건 4방향 다 막혀있다 -> 후진
    else:
    # 3. 후진
    # 3-1. 후진 O -> 뒤로 한 칸 후진 후 Q에 append
    # 3-2. 후진 X -> break
        dir = back(x, y, d)
        nx = x+dr[dir]
        ny = y+dc[dir]
        if MAP[nx][ny] != 1 and 0 <= nx < N and 0 <= ny < M:
            Q.append([nx, ny])
            continue
        break

result = 0
for row in cleaned:
    result += sum(row)
print(result)
