T = int(input())
N = T ** 2
arr = [[0]*T for _ in range(T)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

cnt = 1
dir = 0
while cnt <= N:
    if i < 0 or i > T or j < 0 or j > T:continue
    if arr[i][j+1] == 0:
        arr[i][j] = cnt
    else:
        dir += 1
        i = dr[dir]
        j = dc[dir]

        arr[i][j] = cnt
        cnt += 1
    print(arr)