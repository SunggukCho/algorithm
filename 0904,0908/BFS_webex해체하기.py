"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
#1. 큐생성
#2. 방문배열 생성
#3. 시작정점을 큐에 넣음
#4. 시작정점 방문표시
#5. 큐가 빌 때까지 반복
#6. 큐에서 정점 n을 하나 pop해서 인접한 정점(u)을 큐에 넣음
#7. n에 인접한 정점 중, 아직 방문하지 않은 정점을 큐에 넣음
#8. visit(u) 방문표시
def bfs(v): #v:시작정점
    Q = []
    visited = [0]*(V+1)
    Q.append(v)
    visited[v] = 1

    while Q:
        n = Q.pop(0)
        print(n, end=' ')
        for u in range(1, V+1):
            if adj[n][u] == 1 and visited[u] == 0:
                Q.append(u)
                visited[u] = visited[n]+1
    print(visited)

V, E = map(int, input().split())
edges = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2 = edges[2*i], edges[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

bfs(1)
