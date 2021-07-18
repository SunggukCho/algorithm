'''
1
7
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
'''
import copy
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cores = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == 1:
                cores.append((i, j))

    # 1. 코어 수가 많은 경우의 수 부터 선택, 이때 모두 연결 가능하다면 그 중에서 최소값
    # 2. 만약 그게 안된다면, 코어 수를 하나 빼고 다시 Search

    ans = 0
    visited = copy.deepcopy(arr)
    for core in cores:
        for k in range(4):
            stack = []
            r, c = core
            stack.append((r, c, 0))
            while stack:
                r, c, cnt = stack.pop(0)
                nr = r+dr[k]
                nc = c+dc[k]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                    visited[nr][nc] = cnt+1
                    stack.append((nr, nc, cnt+1))
                if nr == 0 or nr == N-1 or nc == 0 or nc == N-1 and arr[nr][nc] == 0:
                    ans += cnt
                    break

    print('#{} {}'.format(tc, ans))
