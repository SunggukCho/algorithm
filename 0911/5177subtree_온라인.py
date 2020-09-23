"""
풀이접근
subtree의 갯수를 재귀적으로 파악하려고 한다.
후위순회의 형태로 왼쪽의 노드 개수의 합을 구하고, 오른쪽 노드 개수의 합을 구한 뒤 더하면 subtree를 구할 수 있다.
이때 왼쪽도 재귀로, 오른쪽도 재귀로 계속 구하면 된다.
"""
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    L = [0]*(E+2)
    R = [0]*(E+2)
    P = [0]*(E+2)

    arr = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        p, c = arr[i], arr[i+1]

        if L[p]:
            R[p] = c
        else:
            L[p] = c
        P[c] = p

        def traverse(v):
            if v == 0:
                return 0
            return traverse(L[v])+traverse(R[v])+1
    print(traverse(N))