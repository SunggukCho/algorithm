T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    #우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    cnt = 1             #지나가는 순서대로 cnt찍기
    i = j = 0           #arr행,렬
    dir = 0             #탐색 방향
    while cnt <= N**2:  #전체 좌표의 크기는 N^2
        arr[i][j] = cnt #좌표를 순서대로 지나갈때마다 cnt를 넣어준다.
        cnt += 1
        nr = i+dr[dir]  #nr = 기존 i + dr[dir]로 설정하여 방향(dir)을 바꿔야 할 때가 오면 그때 바꿔준다.
        nc = j+dc[dir]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 0:
            # 방향을 바꿔야 할 때: nr,nc가 영역 밖으로 나갔을 때 & arr[nr][nc]가 0이 아닐때(이미 왔었던 곳일때)
            dir = (1+dir)%4 #4로 나눈 나머지에 따라 변경 (초기는 0이므로 우측부터 탐색, 이후 우-하-좌-상 순)
            nr = i+dr[dir]
            nc = j+dc[dir]
        i = nr
        j = nc

    for row in arr:
        print(row)
