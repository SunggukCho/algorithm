'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력결과
1 2 3 4 5 7 6
'''
def bfs(n):
    Q = []
    Q.append(n)
    visited[n] = 1
    while len(Q):
        s = Q.pop(0)
        print(s)
        for w in range(1, N+1):
            if G[s][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[s]+1

N, M = map(int, input().split())
arr = list(map(int, input().split()))
G = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(M):
    s, e = arr[2*i], arr[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

bfs(1)
print(visited)