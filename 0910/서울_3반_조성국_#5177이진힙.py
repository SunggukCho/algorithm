import sys; sys.stdin = open('heap.txt','r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0]*(N+1)
    heapcount = 0
    for i in arr:
        heapcount+=1
        heap[heapcount] = i
        curr = heapcount
        parent = curr//2
        while parent and heap[parent] > heap[curr]:
            heap[parent], heap[curr] = heap[curr], heap[parent]
            curr = parent               #자리 바꾸고 나서도 curr, parent 갱신해줘야 하는데 빼먹었음 ㅠㅠ
            parent = curr // 2

    #print(heap)
    last_idx = N                        #마지막 노드의 idx
    temp = last_idx // 2                #조상 노드의 idx
    temp_list = []                      #조상 노드의 idx들 모음
    while temp != 0:                    
        father = heap[temp]             #조상은 heap의 조상 idx에 있는 값
        temp_list.append(father)        #temp_list에 추가
        temp = temp//2                  #조상 하나 찾았으면 그 위의 조상 찾기 위해 //2 사용

    fathers = sum(temp_list)            #조상값들의 합을 fathers라는 변수에 넣음
    print('#{} {}'.format(tc, fathers))
