'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]

edges = list(map(int, input().split()))

for i in range(E):
    n1, n2 = edges[i*2], edges[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

def dfs(n, V):              #n: 현재 정점
    stack = [0] * V         #스택
    visited = [0] * (V+1)   #방문배열
    top = -1
    top += 1
    stack[top] = n          #시작 정점을 스택에 넣기
    visited[n] = 1          #시작정점을 방문했다고 표시
    #순회 시작
    while top >= 0:         #스택이 비어있지 않는 동안 반복
        n = stack[top]      #스택에서 하나 꺼내옴
        top -= 1            #하나 꺼냈으니까 빼줌
        print(n, end=' ')
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0: #인접하고 아직 방문 하지 않은 정점 i
                top += 1                           #스택에 넣기 전 top을 하나 늘려주고
                stack[top] = i                     #스택에 넣음
                visited[i] = 1                     #스택에 이미 들어갔으니 언젠가 방문할 것. 따라서 바로 방문한 것으로 처리.
                
dfs(1, V)                   #1번 정점을 기준으로 순회
