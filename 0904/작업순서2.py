import sys; sys.stdin = open('bfs.txt','r')

def find(v):
    global visited, count
    count += 1
    if count >=N:
        return
    visited[v] = 1
    if v not in result:
        result.append(v)
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w]==0:
            result.append(w)
            visited[w] = 1
            find(w)
    return

T = 5
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[0]*(N+1) for _ in range(N+1)]

    for i in range(0, len(arr), 2):
        u, v = arr[i], arr[i+1]
        G[u][v] = 1

    start = []
    for i in range(1, N+1):
        cnt = 0
        for j in range(1, N+1):
            if G[j][i] == 0:
                cnt += 1
        if cnt == N:
            start.append(i)
    visited = [0]*(N+1)
    count = 0
    result = []
    for i in range(len(start)):
        find(start[i])

    print('#{} {}'.format(tc, result))
