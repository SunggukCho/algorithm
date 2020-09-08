import sys; sys.stdin = open('graph.txt', 'r')

def BFS(s, e):
    Q = []
    Q.append(s)
    visit[s] = 1
    while Q:
        t = Q.pop(0)
        for w in range(1, V+1):
            if G[t][w] == 1 and visit[w]== 0:
                Q.append(w)
                visit[w] = visit[t] + 1
                if w == e:
                    return visit[e] - visit[s]
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접행렬
    G = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):  # 간선 정보 읽기
        u, v = map(int, input().split())
        G[u][v] = 1
        G[v][u] = 1
    s, e = map(int, input().split())
    visit = [0]*(V+1)  # 방문
    result = BFS(s, e)

    print('#{} {}'.format(tc, result))