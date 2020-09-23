"""
3
4
3 3
0 0 1 0
0 2 0 1
0 0 0 0
1 1 0 2
6
3 2
0 0 0 0 0 0
0 0 3 0 1 1
1 0 0 0 0 0
0 0 3 0 0 2
2 0 0 0 0 0
0 1 0 2 0 2
10
8 7
0 3 0 0 3 0 0 0 0 0
0 3 0 0 0 0 0 1 0 3
0 0 5 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 0 0
0 5 0 0 0 2 0 5 0 0
0 0 0 0 0 3 0 2 0 4
4 0 2 0 0 2 1 4 0 0
0 0 0 0 0 5 0 0 0 0
0 0 0 0 0 0 4 5 5 1
3 0 3 0 2 4 0 0 0 1
"""
"""
풀이접근
1. DFS와 Visited를 사용한다.
2. 값의 크기에 따라 해당 범위만큼 사방 탐색을 한다.
3. 왔던 곳이면 DFS를 하지 않고 처음 온 곳만 한다.
4. DFS가 호출된 숫자를 cnt한다.
"""
def dfs(r, c, d):
    global cnt
    cnt += 1
    visited[r][c] = 1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for j in range(d):  # 사방탐색을 할 때, map에 표기된 숫자만큼 갈 수 있도록 d설정
        for i in range(4):
            nr = r + dr[i] + j * dr[i]  # nr를 설정할 때 j값에 따라 몇 칸 갈 지 설정
            nc = c + dc[i] + j * dc[i]  # nc를 설정할 때 j값에 따라 몇 칸 갈 지 설정
            if 0 <= nr < N and 0 <= nc < N:
                if Map[nr][nc] != 0 and visited[nr][nc] == 0:
                    d = Map[nr][nc]  # 해당 좌표의 Map에 표기된 값으로 d를 재설정
                    dfs(nr, nc, d)

T = int(input())
for tc in range(1, T+1):
    N = int(input())                                            #지도 크기
    R, C = map(int, input().split())                            #최초로 터지는 폭탄의 좌표
    Map = [list(map(int, input().split())) for _ in range(N)]   #폭탄의 위치 Map
    visited = [[0]*N for _ in range(N)]                         #방문 시 표기할 방문배열
    cnt = 0                                                     #dfs함수 호출 cnt

    dfs(R,C,Map[R][C])
    print('#{} {}'.format(tc, cnt))