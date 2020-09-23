import sys; sys.stdin = open('node.txt','r')
"""
풀이접근
재귀로 부모노드의 값을 구함. 왼쪽자식노드+오른쪽자식노드
"""
for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    T = [0]*(N+1)
    for _ in range(M):
        num, val = map(int, input().split())
        T[num] = val

    def dfs(v):
        if v > N: return 0
        l = dfs(v*2)
        r = dfs(v*2+1)
        T[v] += l+r
        return T[v]

    dfs(1)
    print(T[L])
