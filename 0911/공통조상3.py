import sys; sys.stdin = open('same_father.txt', 'r')

def subtree(n):
    global sub
    if tree[n][0]:  # 왼쪽 자식 있으면 sub 하나 추가해주고 다시 재탐색
        sub += 1
        subtree(tree[n][0])  # 재탐색 재귀
    if tree[n][1]:  # 오른쪽 자식 있으면 sub 하나 추가해주고 다시 재탐색
        sub += 1
        subtree(tree[n][1])  # 재탐색 재귀

T = int(input())
for tc in range(1, T + 1):
    # V: 노드 수 E: 간선 수 A:출발점1 B:출발점2
    V, E, A, B = map(int, input().split())
    arr = list(map(int, input().split()))
    # 완전 이진트리가 아닌 경우 2차원으로 트리 생성, but VxV 크기로는 너무 커짐
    tree = [[0]*3 for _ in range(V+1)]
    for i in range(E):
        s, e = arr[2*i], arr[2*i+1]
        if tree[s][0] == 0:  # 왼쪽 자식
            tree[s][0] = e
        else:
            tree[s][1] = e  # 오른쪽 자식
        tree[e][2] = s  # 부모
    #부모노드 찾기
    parents_A = []
    parents_B = []
    child = A
    #A의 부모찾기
    while tree[child][2]:       #부모노드에 빈 자리 나올때까지 순회
        parent = tree[child][2]
        parents_A.append(parent)
        child = tree[child][2]
    #B의 부모 찾기, 공통조상 찾자마자 break
    kid = B
    parent_node = 1                 #공통조상 초기값 1로 설정
    while tree[kid][2]:
        parent = tree[kid][2]
        parents_B.append(parent)
        if parent in parents_A:
            parent_node = parent    #공통조상 발견하면 갱신, 없으면 그냥 1로
            break
        kid = tree[kid][2]

    sub = 1     #자기자신부터 세고 시작해야하므로 초기값 1 설정
    subtree(parent_node)
    print('#{} {} {}'.format(tc, parent_node, sub))
