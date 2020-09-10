#DFS 아닌 방법으로
"""
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
"""
T = 1
for tc in range(1,T+1):
    N = int(input())
    tree = [0]*(N+1)        #완전 이진 트리이므로 1차원 배열로 가능
    for i in range(N):
        node = list(input().split())
        tree[int(node[0])] = node[1]
    print(tree)