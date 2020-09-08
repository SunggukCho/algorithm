"""
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
"""
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def dfs(x, y, string):
    global result
    if len(string) == 7:
        if string not in result:
            result.add(string)
    for k in range(4):
        nr = x+dr[k]
        nc = y+dc[k]
        if nr >= 0 and nr < 4 and nc >= 0 and nc < 4 and len(string) <= 7:
            dfs(nr, nc, string+arr[nr][nc])

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    result = set()
    string = ''
    for i in range(4):
        for j in range(4):
            dfs(i,j,arr[i][j])
    print('#{} {}'.format(tc,len(result)))