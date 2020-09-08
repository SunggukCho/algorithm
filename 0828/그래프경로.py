def DFS(v):
    visit[v] = 1
    if v == e:
        return 1
    for w in range(1, V+1):
        if G[v][w] == 1 and visit[w]==0:    #인접 정점 있음, 동시에 방문 여부 체크
            if DFS(w) == 1:
                return 1
    return 0

for tc in range(1, int(input()) +1):
    V, E = map(int, input().split())
    #인접행렬
    G = [[0]*(V+1) for _ in range(V+1)

    for _ in range(E):
        u, v = map(int, input().split())
        G[u][v] = 1         #유향 그래프이므로 한 번만 해준다. G[v][u]= 1 필요 없음

    s, e = map(int, input().split())
    visit = [0] * (V+1)

    DFS(s)