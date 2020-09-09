import heapq

heap = [7,2,5,3,4,6]
## 1. 최소 heap으로 만들기
#heapify 전
print(heap)
#heapify 후
heapq.heapify(heap)
print(heap)
## 2. heappush
heapq.heappush(heap, 1)
print(heap)
## 3. heappop
while heap:
    print(heapq.heappop(heap), end=' ')
print()
## 4. 최대 heap
temp = [7,2,5,3,4,6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i], temp[i]))
heapq.heappush(heap2, (-1, 1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1], end=' ')
