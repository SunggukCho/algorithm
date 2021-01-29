'''
5
3 2 1
1 2
2 3
2
3 2 1
1 2
2 3
1
4 3 2
1 2
2 3
4 1
1
4
6 3 3
1 2
3 5
4 6
1
3
4
6 3 3
1 2
3 5
4 6
2
5
6
#답:2
#답:3
#답:4
#답:6
#답:3

'''
'''
## 첫 번째 try
-> 재귀 방식으로 풀이
-> 런타임 에러
## 두 번째 try -> 시간초과
T = int(input())
for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    z = [int(input()) for _ in range(l)]
    fall = [0]*(n+1)            #해당 번호 도미노가 넘어지면 1로 표기
    arr.sort()

    for i in range(l):
        pick = z[i]    #손으로 넘기는 도미노 번호
        fall[pick] = 1  #일단 손으로 넘기는 도미노는 무조건 fall
        while len(arr): #손으로 넘기는 도미노 뒤에 연결된 도미노를 찾아 연쇄적으로 넘겨준다
            for j in range(len(arr)):
                if arr[j][0] == pick:
                    next = arr[j][1]
                    arr.pop(j)
                    break
            if fall[next] == 0:
                fall[next] = 1
                pick = next
            else:
                break

    print(fall.count(1))
'''
# 세 번째 try
## domino 값을 받을 때부터 dict로 연결시켜 속도향상을 노림.
## queue도 deque를 사용
from collections import deque
T = int(input())
for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    domino = dict()
    for i in range(m):
        x, y = map(int, input().split())
        domino[x] = y
    fall = [0]*(n+1)            #해당 번호 도미노가 넘어지면 1로 표기

    for i in range(l):
        z = int(input())
        Q = deque()
        Q.append(z) #손으로 넘기는 도미노 번호 Q에 추가
        while Q:  # 손으로 넘기는 도미노 뒤에 연결된 도미노를 찾아 연쇄적으로 넘겨준다
            tmp = Q.popleft()
            fall[tmp] = 1       #손으로 넘기는 것은 무조건 1처리, 이후 들어오는 값들도 처리
            
    print(sum(fall))
