def dfs(r,c):
    arr[r][c] = 2      #방문하면 2로 넣어줌
    for k in range(4):  #4방 탐색이므로 range(4)
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue     #벗어나면 빠져나가라
        if arr[nr][nc] == 0 or arr[nr][nx] == 2: continue       #가려는 곳이 0이면 넘어가라
        dfs(nr, nc)

#상하좌우
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            dfs(i,j)