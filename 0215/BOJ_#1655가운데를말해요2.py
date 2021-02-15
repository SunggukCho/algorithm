'''
BOJ_#1655가운데를말해요2 - 오답
https://www.acmicpc.net/problem/1655
이진탐색 스타일로 재시도
어김없이 시간초과

7
1
5
2
10
-99
7
5
'''
from collections import deque
T = int(input())
left = deque()
right = deque()

for tc in range(1, T+1):
    N = int(input())
    if len(left) == len(right):
        #left에 append
        if len(left) == 0:
            left.append(N)
        elif left[-1] < N:
            left.append(N)
        else:
            left.insert(0, N)
    else:
        #right 앞으로 insert
        if len(right) == 0:
            right.append(N)
        elif right[0] > N:
            right.insert(0, N)
        else:
            right.append(N)
    ans = left[-1]
    print(ans)
