T = int(input())                     #테스트 수
for tc in range(T):
    N = int(input())                 #N x N 배열

    arr = [[0 for i in range(N)] for i in range(N)]
    # 순서 -> 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    i = 0
    for i in range(N):
        for j in range(N):
            nr = j+dr[i]
            nc = j+dc[i]
