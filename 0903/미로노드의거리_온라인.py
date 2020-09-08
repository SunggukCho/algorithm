import sys; sys.stdin = open('miro2.txt','r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    sx = sy = ex = ey = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                sx, sy = i, j
            elif maze[i][j] == '3':
                ex, ey = i, j

    visit = [[0]*N for _ in range(N)]
    Q = [[sx, sy]]
    visit[sx][sy] = 1

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            tx, ty = x+dx[i], y+dy[i]
            #경계체크, 통로인지, 방문정보
            if tx < 0 or tx==N or ty < 0 or ty ==N: continue
            if maze[tx][ty] == '1' or visit[tx][ty] != 0:continue        #1: 벽을 만났을 때, 2. 방문했으면 pass
            visit[tx][ty] = visit[x][y] + 1
            Q.append([tx, ty])

    print(visit[ex][ey]-2)          #출발, 도착지까지 합해진 값이므로 -2
    print(visit)