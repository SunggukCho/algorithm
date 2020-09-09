import sys; sys.stdin = open('contact.txt','r')

def BFS(v):
    Q = []
    Q.append(v)
    visit[v] = 1

    while Q:
        v = Q.pop(0)
        for w in range(1, 101):
            if G[v][w] == 1 and visit[w] == 0:
                visit[w] = visit[v] + 1
                Q.append(w)
    ans = 1
    for i in range(2, 101):
        if visit[ans] <= visit[i]:
            ans = i
    print('#{} {}'.format(tc,ans))
T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    data = []
    for i in range(0, len(arr), 2):
        data.append([arr[i], arr[i+1]])

    #최대값
    G = [[0]*101 for _ in range(101)]                 #인접행렬
    visit = [0]*101                                   #방문
    for i in data:
        x = i[0]
        y = i[1]
        G[x][y] = 1

    #start = 초기 시작점
    visit[start] = 1
    BFS(start)
