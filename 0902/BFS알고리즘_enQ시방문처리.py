#1. enQ시 방문 처리 - 출발점에서 얼만큼 떨어져 있는지 visited로 확인이 가능하다는 장점이 있다.
def BFS(G, V):
    visited = [0]*(n+1)
    q = []
    q.append(v)
    visited[v]=1

    while len(q) != 0:
        t = q.pop(0)
        for w in G[t]:
            if not visited[w]:              #방문하지 않은 곳이라면
                q.append(w)                 #enQueue
                visited[w] = visited[t] +1  #방문한 것으로 표시

