import sys; sys.stdin = open('graph_input.txt', 'r')

def dfs(s):
    global e
    visit[s] = 1
    if s == e:
        return 1
    for w in range(1, N+1):
        if arr[s][w] == 1 and visit[w] ==0:
            dfs(w)
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        u, v = map(int, input().split())
        arr[u][v] = 1
        arr[v][u] = 1
    s, e = map(int, input().split())

    visit = [0]*(N+1)

    print(dfs(s))