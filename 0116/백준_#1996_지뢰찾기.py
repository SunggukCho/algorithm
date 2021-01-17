"""
5
1....
..3..
.....
.4...
...9.
"""
dr = [-1, 0, 1, 0, -1, 1, 1, -1]
dc = [0, 1, 0, -1, 1, 1, -1, -1]
T = int(input())
arr = [list(input()) for _ in range(T)]
MAP = [[0]*T for _ in range(T)]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == '.':
            num = 0
            for k in range(8):
                nr = i+dr[k]
                nc = j+dc[k]
                if 0 <= nr < T and 0 <= nc < T and arr[nr][nc] != '.':
                    num += int(arr[nr][nc])
            if num >= 10:
                MAP[i][j] = 'M'
            else:
                MAP[i][j] = str(num)
        else:
            MAP[i][j] = '*'
for row in MAP:
    for r in row:
        print(r, end='')
    print()
