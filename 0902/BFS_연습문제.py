"""
입력
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
#0. 입력
V, E = map(int, input().split())       #vertex, edges
temp = list(map(int, input().split()))
G = [[0]*(V+1) for _ in range(V+1)]     #Graph, 인접행렬 G

# 1. 인접행렬 만들기
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]       #start, end; 간선 갯수 E만큼 돌면서 홀수짝수 두 개 씩 s, e에 넣어줌.
    G[s][e] = G[e][s] = 1               #인접행렬에 넣어줌

#인접행렬 출력
# for i in range(1, V+1):
#     print('{} {}'.format(i, G[i]))

# 2. BFS 함수 만들기
def bfs(v):
    #필요한 것: 큐, 방문
    Q = []
    visit = [0]*(V+1)

    #enQ(v), visit(v)
    Q.append(v)
    visit[v] = 1
    print(v, end=' ')

    #큐가 비어있지 않은 동안
    while Q:
        #v = deQ() -> Q.pop()
        v = Q.pop(0)
        #v의 인접한 정점(w)가 방문 안한 정점이면 enQ하고 방문처리
            #enQ(w), 방문처리(w)
        for w in range(1, V+1):
            if G[v][w] == 1 and visit[w] == 0:
                Q.append(w)
                visit[w] = 1
                print(w, end=' ')

bfs(1)