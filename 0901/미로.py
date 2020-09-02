"""
1. 출발점 찾기
2. 4방 탐색을 하면서 0인 점들을 stack에 쌓고 visited에 추가하기
3. 계속 따라가다가 더 이상 0 또는 3이 나오지 않으면 stack.pop()해서 뒤로 간다음 안 간 곳 서치하기
4. 3찾으면 return 1, 못찾으면 return 0
"""
import sys; sys.stdin = open('miro.txt', 'r')

def dfs(arr, x, y):
    #상-시계방향 4방탐색
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    stack = []
    global visited, result
    visited[x][y] = 1

    for i in range(4):
        nr = x+dr[i]
        nc = y+dc[i]
        if nr < 0 or nr >= len(arr) or nc < 0 or nc >= len(arr): continue
        if arr[nr][nc] == 3:
            stack.append((nr, nc))
            result += 1
        if arr[nr][nc] == 0 and visited[nr][nc] == 0:
            stack.append((nr,nc))
            dfs(arr, nr, nc)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    result = 0

    start_x = start_y = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 2:
                start_x, start_y = i, j

    dfs(board, start_x, start_y)
    print('#{} {}'.format(tc,result))