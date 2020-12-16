import sys; sys.stdin = open('miro1226.txt')

def dfs(r,c):
    global flag
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited[r][c] = 1
    for k in range(4):
        nr = r+dr[k]
        nc = c+dc[k]
        if arr[nr][nc] == 3:
            flag = 1
            return flag
        elif arr[nr][nc] == 0 and visited[nr][nc] == 0:
            dfs(nr, nc)

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    flag = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                dfs(i,j)

    print('#{} {}'.format(tc, flag))
