import sys; sys.stdin = open('node.txt','r')

T = int(input())
for tc in range(1, T+1):
    #N:노드의 수 M:리프노드의 수 L: 출력할 노드의 번호
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    tree = [0]*(N+1)                #트리 만들기
    for i in arr:                   #i[0]: 위치, i[1]: 값
        tree[i[0]] = i[1]
    last_idx = 0
    while tree[1] == 0:             #트리의 루트를 채울 때 까지 반복
        for i in range(len(tree)):
            if tree[i] == 0:
                idx = i
                if idx > last_idx:
                    last_idx = idx  #트리에 비어있는 노드의 최대 idx = last_idx
        # last_idx는 0인 마지막 idx
        parent = last_idx
        if last_idx*2+1 <= N:
            child1, child2 = tree[last_idx*2], tree[last_idx*2+1]
            tree[parent] = child1+child2
        else:
            child1 = tree[last_idx*2]
            tree[parent] = child1
        last_idx = parent-1             #last_idx 갱신
    print('#{} {}'.format(tc, tree[L]))
