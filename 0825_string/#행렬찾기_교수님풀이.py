'''
1
8
1 2 3 0 0 4 5 0
6 7 8 0 0 0 0 0
9 1 2 0 0 3 0 0
4 5 6 0 0 7 0 0
0 0 0 0 0 8 0 0
9 1 2 3 0 4 0 0
5 6 7 8 0 9 0 0
0 0 0 0 0 0 0 0
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    answer = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] :                           #0이면 false, 0아니면 True
                x = i
                while x < N and arr[x][j] != 0:      #영역을 벗어나지 않고 0이 아닐 동안 반복
                    y = j
                    while y < N and arr[x][y] != 0:
                        arr[x][y] = 0
                        y += 1
                    x += 1
                answer.append((x-i,y-j))

    for i in range(len(answer)-1):                     #버블 정렬
        idx = i
        for j in range(i+1, len(answer)):
            #조건 2개
            #1. 행렬의 크기
            a = answer[idx][0] * answer[idx][1]
            b = answer[j][0] * answer[j][1]
            if a > b:
                idx = j
            elif a == b and answer[idx][0] > answer[j][0]: #2. 행렬의 크기가 같으면 행으로 비교
                idx = j
        answer[i], answer[idx] = answer[idx], answer[i]

    print('#%d %d' %(tc, len(answer)), end="")
    for a,b in answer:
        print(" %d %d" %(a,b), end="")
    print()