import sys; sys.stdin = open('same_father.txt','r')
def subtree(n):
    global sub
    # 말단 노드이면 재귀호출 X
    if n in leafs:
        return
    for i in range(1, V + 1):
        if tree[n][i]:  #자식 있으면 sub 하나 추가해주고 다시 재탐색 
            sub += 1
            subtree(i)  # 재탐색 재귀

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
            leafs.remove(parent)                #leafs에는 말단 노드들만 모여있음
    #트리의 열 순회하면서 부모 노드 찾기
    parents_A = []                    #A의 부모 노드들 아래 계층부터 표기
    parents_B = []                    #B의 부모 노드들 아래 계층부터 표기
    visited_A = [0]*(V+1)
    visited_B = [0]*(V+1)
    parent_node = 1                   #A, B의 공통 조상 노드
    #parent_node의 A,B 각각의 첫자식
    first_A = 0
    first_B = 0
    #A, B 부모노드 리스트 찾기
    #A 조상찾기
    kid = A
    while True:
        for i in range(1, V+1):
            if tree[i][kid] == 1:
                parents_A.append(i) #조상노드들의 리스트
                kid = i             #부모를 새로운 자식으로 갱신
        if kid == 1:                #1까지 왔으면 다 온거임
                break
    #B조상찾기 - 찾는 도중 A 조상들이 있는 parents_A리스트에 있는지 체크해서 있으면 break.
    kid = B
    while True:
        for i in range(1, V+1):
            if tree[i][kid] == 1:
                kid = i             #부모를 새로운 자식으로 갱신
                parents_B.append(i)
                if i in parents_A:
                    parent_node = i
                    break
        if kid == 1 or parent_node != 1:
            break
    #parent_node 아래 subtree의 노드 수 구하기
    #전위순회 방법 사용
    sub = 1
    visited = [0]*(V+1)
    #parent 노드의 첫 자식
    first_A = parents_A[-1]
    first_B = parents_B[-2]
    subtree(parent_node)

    print('#{} {} {}'.format(tc, parent_node, sub))
    