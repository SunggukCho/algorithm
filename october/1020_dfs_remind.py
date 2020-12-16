'''
dfs

정점, 간선수
간선정보
시작점 : 1

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력결과
1 3 7 6 5 4 2
'''
def dfs(v):
    global stack
    print(v)
    visited[v] = 1
    adj = []
    for i in range(len(G[v])):
        if G[v][i] == 1:
            adj.append(i)
    while len(adj) != 0:
        s = adj.pop()
        if visited[s] == 0:
            dfs(s)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
G = [[0](N+1) for _ in range(N+1)]
visited = [0](N+1)

for i in range(M):
    s, e = arr[2*i], arr[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1)

