import sys; sys.stdin = open('same_father.txt','r')

def dfs(n, visited, parents):
    for j in range(1, V + 1):
        if tree[j][n] == 1 and visited[n] == 0:
            visited[n] = 1
            parents.append(n)
            dfs(j, visited, parents)
    return
def dfs_2(n, visited, parents):
    global parents_A, parent_node
    for j in range(1, V + 1):
        if tree[j][n] == 1 and visited[n] == 0:
            visited[n] = 1
            if n in parents_A:
                parent_node = n
                return
            parents.append(n)
            dfs_2(j, visited, parents)
    return
def subtree(n):
    global sub
    visited[n] = 1
    for i in range(1, V+1):
        #말단 노드이면 재귀호출 X
        if n in leafs:continue
        if tree[n][i] and not visited[i]:
            sub += 1
            subtree(i)

T = int(input())
for tc in range(1, T+1):
    #V: 노드 수 E: 간선 수 A:출발점1 B:출발점2
    V, E, A, B = map(int, input().split())  
    arr = list(map(int, input().split()))
    #완전 이진트리가 아닌 경우 2차원으로 트리 생성
    tree = [[0]*(V+1) for _ in range(V+1)]
    #트리에 값 넣기
        #말단 노드 따로 빼놓기
    leafs = set(arr)
    for i in range(0, E):
        parent, child = arr[2*i], arr[2*i+1]
        tree[parent][child] = 1
        if parent in leafs:
            leafs.remove(parent)
    #트리의 열 순회하면서 부모 노드 찾기
    parents_A = []                    #A의 부모 노드들 아래 계층부터 표기
    parents_B = []                    #B의 부모 노드들 아래 계층부터 표기
    visited_A = [0]*(V+1)
    visited_B = [0]*(V+1)
    #A, B 부모노드 리스트 찾기
    parent_node = 0
    dfs(A, visited_A, parents_A)
    dfs_2(B, visited_B, parents_B)
    #A와 B의 가장 가까운 부모노드 찾기
    # for i in parents_A:
    #     if i in parents_B:
    #         parent_node = i
    #         break
    #만약 parent node가 없다면 root가 parent노드이다
    if parent_node == 0:
        parent_node = 1
    #parent_node 아래 subtree의 노드 수 구하기
    #전위순회 방법 사용
    sub = 1
    visited = [0]*(V+1)
    subtree(parent_node)

    print('#{} {} {}'.format(tc, parent_node, sub))
