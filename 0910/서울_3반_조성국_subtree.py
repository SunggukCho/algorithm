import sys; sys.stdin = open('subtree.txt','r')
def dfs(v):
    global cnt
    visited[v] = 1
    for i in range(1, E+2):
        if tree[v][i]==1 and visited[i] == 0:
            cnt += 1
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[0]*(E+2) for _ in range(E+2)]

    for i in range(E):
        tree[arr[2*i]][arr[2*i+1]] = 1
    visited = [0]*(E+2)

    cnt = 1
    dfs(N)
    print('#{} {}'.format(tc, cnt))


