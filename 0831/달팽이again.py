T = int(input())
N = T ** 2
arr = [[0]*T for _ in range(T)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

cnt = 1
dir = 0
while cnt <= N:
    nr = 0
    nc = 0
    if nr >= 0 and nr < len(arr) and nc >= 0 and nc < len(arr):
        arr[nr][nc] = cnt
        nr = dr[dir]
        nc = dc[dir]
