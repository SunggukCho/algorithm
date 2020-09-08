#2. deQ시 방문처리
def BFS(G, v):              #그래프 G, 탐색 시잠점 v
    visited = [0]*n         #n 정점 개수
    queue = []
    queue.append(v)         #시작점 큐 삽입
    while queue:            #Q 비어있지 않은 경우
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            visit(t)
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)
