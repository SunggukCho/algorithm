import sys;sys.stdin = open('s_input.txt','r')

def dfs(v, N):
    global result
    stack = [0] * N  # 스택
    top = -1
    top += 1
    stack[top] = v  # 시작 정점을 스택에 넣기
    visited[v] = 1  # 시작정점을 방문했다고 표시
    # 순회 시작
    while top >= 0:  # 스택이 비어있지 않는 동안 반복
        n = stack[top]  # 스택에서 하나 꺼내옴
        top -= 1  # 하나 꺼냈으니까 빼줌
        for i in range(1, N+1):
            if G[n][i] == 1 and visited[i] == 0:  # 인접하고 아직 방문 하지 않은 정점 i
                top += 1  # 스택에 넣기 전 top을 하나 늘려주고
                stack[top] = i  # 스택에 넣음
                visited[i] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    G = [[0]*(N+1) for _ in range(N+1)]

    for i in range(len(arr)):
        u, v = arr[i][0], arr[i][1]
        G[u][v] = 1
        G[v][u] = 1

    cnt = 0
    visited = [0] * (N+1)  # 방문배열
    #DFS를 한 바퀴 돌면서 방문하는 인덱스를 result에 추가. 이전 result 없는 것들만 추가하고, 추가 될 때마다 cnt +=1.
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i, N)
            cnt += 1
    print('#{} {}'.format(tc, cnt))