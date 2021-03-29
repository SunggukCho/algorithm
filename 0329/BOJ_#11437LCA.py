'''
BOJ_#11437LCA
https://www.acmicpc.net/problem/11437

두 노드 중 한쪽에서 조상 노드를 쭉 찾는다.
나머지 한 노드에서 조상노드를 쭉 찾으면서 공통되는게 있으면 break-> 그게 LCA이다.
만약 끝까지 다 돌면 루트가 공통노드.

난관 1. 아니 ㅅㅂ input이 부모-자식순이 아니네? 2차원 배열로 받으면 N이 50000까지라서 메모리 무조건 터질거 같은데...
난관 2.
'''
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split()) #그냥 두 노드
    tree[u].append(v)
    tree[v].append(u)
# print(G)
M = int(input())
for _ in range(M):
    x, y = map(int, input().split())



