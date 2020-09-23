"""
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
"""
def check(arr):
    global cnt
    cnt = 0
    #가로
    for i in range(5):
        col = 0
        for j in range(5):
            col += arr[i][j]
        if col == 5:
            cnt += 1
            if cnt == 3:
                return
    #세로
    for i in range(5):
        row = 0
        for j in range(5):
            row += arr[j][i]
        if row == 5:
            cnt += 1
            if cnt == 3:
                return
    #대각 우하향
    cross = 0
    for k in range(5):
        cross += arr[k][k]
        if cross == 5:
            cnt += 1
            if cnt == 3:
                return
    # 대각 우상향
    cross = 0
    for k in range(5):
        cross += arr[4-k][k]
        if cross == 5:
            cnt += 1
            if cnt == 3:
                return

board = [list(map(int, input().split())) for _ in range(5)]  #빙고판
calls = []      #사회자 콜
for i in range(5):
    arr = list(map(int, input().split()))
    for j in arr:
        calls.append(j)

cnt = 0
visited = [[0]*5 for _ in range(5)]
for k in range(len(calls)):
    for i in range(5):
        for j in range(5):
            if board[i][j] == calls[k]:
                visited[i][j] = 1
    check(visited)
    if cnt == 3:
        print(k+1)
        break
