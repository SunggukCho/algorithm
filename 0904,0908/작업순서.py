import sys; sys.stdin = open('bfs.txt','r')
def check(w):
    for i in range(1, N+1):
        count = 0
        for w in range(1, N+1):
            if G[w][i] == 0:
                count += 1
        if count == N:
            return 1
        else:
            return 0

def bfs(v):
    visited = [0]*(N+1)
    Q = []
    Q.append(v)
    while Q:
        t = Q.pop(0)
        for w in range(1, N+1):
            if G[t][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[t] +1
    return visited

T = 10
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

    result = bfs(start[0])
    idx = []
    for i in result:
        if i != 0:
            idx.append([i, result.index(i)])
    idx.insert(0, [0, start[0]])
    new_idx = sorted(idx, key=lambda x:x[0])
    ans = ''
    for i in new_idx:
        ans += str(i[1]) + ' '
    # print('#{} {}'.format(tc, ans))
