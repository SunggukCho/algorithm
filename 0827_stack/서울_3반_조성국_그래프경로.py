import sys
sys.stdin = open('graph.txt', 'r')

def dfs(s):
    global g, e, result
    visited[s] = 1
    for w in range(1, v+1):
        if Map[s][w] == 1 and visited[w] == 0:
            if w == g:
                result += 1
            else:
                dfs(w)

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    Map = [[0]*(v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    for i in range(e):
        start, end = map(int, input().split())
        Map[start][end] = 1
    s, g = map(int, input().split())
    stack = []
    result = 0
    dfs(s)
    print(result)
    # if result:
    #     print('#{} {}'.format(tc, 1))
    # else:
    #     print('#{} {}'.format(tc, 0))
