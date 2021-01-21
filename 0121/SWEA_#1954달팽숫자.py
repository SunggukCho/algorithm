# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    num = 1
    turn = 0
    r = c = 0
    while num <= N**2:
        if arr[r][c] == 0:
            arr[r][c] = num

        if 0 <= r + dr[turn % 4] < N and 0 <= c + dc[turn % 4] < N:
            if arr[r + dr[turn % 4]][c + dc[turn % 4]] != 0:
                turn += 1
        else:
            turn += 1
        r = r + dr[turn % 4]
        c = c + dc[turn % 4]
        num += 1
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
