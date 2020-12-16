"""
풀이
1. 0이 있는지 없는지 체크한다. 없으면 0출력하고 끝
2. 0이 있다면, 익은 토마토(1)을 구한다.
3. 익은 토마토(1) 주변을 사방탐색하며 0이면 1로 변경한다.
4. 이 과정의 숫자를 반복하고 cnt를 올려준다.
5. 만약 이전 바구니의 모양과 현재 바구니의 모양이 같다면 변화가 일어나지 않았으므로 불가능(-1)을 출력한다.
6. 만약 모든 작업(DFS)가 끝나면 몇 번만에 끝났는지 cnt를 출력한다.

"""
import copy
def bfs(r, c):
    visited[r][c] = 1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for k in range(4):
        nr = r+dr[k]
        nc = c+dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                arr[nr][nc] = 1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
cnt = 0

zeros = []
ones = []
minus = []

cnt = 0
while True:
    old_arr = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                zeros.append([i,j])
            elif arr[i][j] == 1:
                ones.append([i,j])

    if cnt == 0 and len(zeros) == 0:
        print('0')
        break
    else:
        for k in ones:
            r, c = k[0], k[1]
            bfs(r, c)
        if old_arr == arr:
            if len(zeros) == 0:
                print(cnt)
            else:
                print('-1')
            break
        else:
            cnt += 1
            zeros = []
            ones = []
            minus = []
            continue
