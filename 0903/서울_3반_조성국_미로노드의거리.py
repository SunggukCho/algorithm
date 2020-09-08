import sys; sys.stdin = open('miro2.txt','r')

def bfs(x, y):
    global result, dist
    dr = [-1, 0 , 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(4):
        nr = x+dr[i]
        nc = y+dc[i]
        if nr >= 0 and nr < N and nc >= 0 and nc < N and visit[nr][nc] == 0:
            if arr[nr][nc] == 3:                    #도착하면
                visit[nr][nc] = visit[x][y] + 1     #도착지점에 visit 표시하고
                result += 1                         #result 1로 도착할 수 있다는 표시하고
                dist = visit[nr][nc] - visit[start_x][start_y] -1   #거리는 도착점에서 출발점의 값을 뺀다
                return 1
            elif arr[nr][nc] == 0:
                visit[nr][nc] = visit[x][y]+1       #출발점에서부터 0으로 한 칸씩 전진할 때마다 +1해준다
                bfs(nr, nc)                         #아직 도착하지 못했으므로 재귀함수 호출

    return 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visit = [[0]*(N) for _ in range(N)]
    #출발 좌표 정하기
    start_x = 0
    start_y = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_x = i
                start_y = j
                break
    visit[start_x][start_y] = 1
    result = dist = 0                   #result는 3에 도착할 수 있는지 없는지, dist는 거리
    bfs(start_x, start_y)

    if result:
        print('#{} {}'.format(tc, dist))
    else:
        print('#{} {}'.format(tc, result))  #결과값 없으면 0출력
