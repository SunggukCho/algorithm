import sys; sys.stdin = open('bfs.txt','r')

def find(v):
    global visited, count, upper
    count += 1
    if count >=N:
        return
    visited[v] = 1
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w]==0 and col_sum[w-1] <= 1:
            result.append(w)
            visited[w] = 1
            find(w)
        elif G[v][w] == 1 and col_sum[w-1] >= 2:
            col_sum[w-1] -= 1
    return

T = 10
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[0]*(N+1) for _ in range(N+1)]

    for i in range(0, len(arr), 2):
        u, v = arr[i], arr[i+1]
        G[u][v] = 1

    start = []
    col_sum = []
    for i in range(1, N+1):
        cnt = 0
        for j in range(1, N+1):
            if G[j][i] == 0:
                cnt += 1
        col_sum.append(N-cnt)
        if cnt == N:
            start.append(i)
    visited = [0]*(N+1)
    count = 0
    result = []
    upper=[]
    for i in start:
        result.append(i)
        find(i)

    ans = ''
    for i in result:
        ans += str(i)+' '
    print('#{} {}'.format(tc, ans))
