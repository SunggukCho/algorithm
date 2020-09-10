import sys;sys.stdin = open('s_input.txt','r')

def dfs(cur):
    visited[cur] = 1
    for i in range(1, N+1):
        if G[cur][i] == 1 and visited[cur]==0:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    G = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(len(arr)):
        u, v = arr[i][0], arr[i][1]
        G[u][v] = 1
        G[v][u] = 1

    cnt = 0
    visited = [0]*(N+1)
    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(cnt)