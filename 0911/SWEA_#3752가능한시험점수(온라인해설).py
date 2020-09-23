"""
시간초과를 막기 위한 백트래킹
첫 번 째 문제를 틀리면 왼쪽, 맞추면 오른쪽으로 나누는 트리를 만든다
"""
"""
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1
"""
### 깊이 우선 탐색(DFS) - 이것도 시간초과임  ###
for tc in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))
    visit = [0]*(sum(score)+1)

    def dfs(k,s):
        if k == N:
            visit[s] = 1
        else:
            dfs(k+1, s)             #k번 문제를 틀린 경우
            dfs(k+1, s+score[k])    #k번 문제를 맞은 경우, score를 추가해줌
    dfs(0,0)
    print('#{} {}'.format(tc, sum(visit)))
#########################################################################
###### BFS 개념 이지만 이것도 시간초과임 #######
for tc in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))
    visit = [0]*(sum(score)+1)
    Q = [[0, 0]]
    while Q:
        k, s = Q.pop(0)
        if k == N:
            visit[s] = 1
        else:
            Q.append([k+1, s])
            Q.append([k+1, s+score[k]])
    print('#{} {}'.format(tc, sum(visit)))

##### 백트래킹이 들어가야 함 #######