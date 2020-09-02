#1. enQ시 방문 처리
BFS(G, V):
visited = [0]*(n+1)
q = []
q.append(v)
visited[v]=1

while len(q)!= 0:
    t = q.pop()
    for w in G[t]:
        if not visited[w]:          #방문하지 않은 곳이라면
            q.append(w)             #enQueue
            visited[w]
