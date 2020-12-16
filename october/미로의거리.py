def dfs(r,c):
    global cnt
    Q = []
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for k in range(4):
        nr = r+dr[k]
        nc = c+dc[k]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            Q.append([nr, nc])
    while len(Q):
        deque = Q.pop(0)
        x, y = deque[0], deque[1]
        if arr[x][y] == 0 and visited[x][y] == 0:
            dist = abs(r-x)+abs(c-y)
            visited[x][y] = dist
            for k in range(4):
                nx = x + dr[k]
                ny = y + dc[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] == 0:
                        Q.append([nx, ny])
                    elif arr[nx][ny] == 3:
                        dist = abs(nx-r)+abs(ny-c)
                        return dist
        elif arr[x][y] == 3:
            return dist
            break
        elif arr[x][y] == 1: continue
        elif len(Q) == 0:
            return 0

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    cnt = 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                result = dfs(i,j)
    if result != 0:
        print('#{} {}'.format(tc, result-1))
    else:
        print('#{} {}'.format(tc, 0))
