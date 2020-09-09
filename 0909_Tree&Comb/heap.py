def heappush(value):
    global heapcount
    heapcount+=1                        #지금 들어온 원소가 저장될 위치
    heap[heapcount] = value             #들어온 원소 값 집어넣기
    current = heapcount                 #현재 위치 = heapcount
    parent = current//2                 #부모의 위치 = heapcount//2
    # 1. 루트가 아니고
    # 2. 부모 노드 값 > 자식 노드 값보다 크면 SWAP
    while parent and heap[parent] > heap[current]:
        heap[parent], heap[current] = heap[current], heap[parent]
        current = parent
        parent = current // 2

def heappop():
    global heapcount
    retValue = heap[1]          #
    heap[1] = heap[heapcount]   #
    heap[heapcount] = 0         #원래 있던 자리 0
    heapcount -= 1
    parent = 1
    child = parent * 2          #왼쪽자식

    if child + 1 <= heapcount:  #오른쪽 자식 존재, => 비교
        if heap[child] > heap[child+1]: #오른쪽 자식이 더 작으면 바꿔라
            child = child+1
    #자식 노드가 존재하고, 부모 노드 > 자식노드 이면, SWAP
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent *2
        if child + 1 <= heapcount:  # 오른쪽 자식 존재, => 비교
            if heap[child] > heap[child + 1]:  # 오른쪽 자식이 더 작으면 바꿔라
                child = child + 1
    return retValue
#최소힙
heapcount = 0           #마지막 원소가 들어갈 위치
temp = [7,2,5,3,4,6]
N = len(temp)
heap=[0]*(N+1)

for i in range(N):
    heappush(temp[i])
print()