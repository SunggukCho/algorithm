"""
입력
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def bfs(v):
    Q = []
    Q.append(v)
    visit[v] = 1
    print(v, end=' ')

    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = 1
                print(w, end=' ')

V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[] for _ in range(V+1)]
visit = [0] * (V+1)

for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s].append(e)
    G[e].append(s)

bfs(1)
print()
#Q. 1번에서 가장 멀리 있는 정점의 번호는 얼마이고 몇 칸 떨어져 있을까?
maxI = 0
for i in range(1, V+1):
    if visit[maxI] < visit[i]:
        maxI = i
print(maxI, visit[maxI]-1)
