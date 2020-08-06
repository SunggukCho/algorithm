import sys
sys.stdin = open('fly.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    #변수 입력
    N, M = map(int, input().split())
    #N :행, 열의 길이, M: 파리채 크기
    arr = []

    #우 -> 우하 -> 하 -> 본인
    dr = [0, 1, 1, 0, ]
    dc = [1, 1, 0, 0, ]

    for i in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)

    sum_arr = []
    for i in range(N-1):
        for j in range(N-1):
            temp = 0
            for k in range(4):
                testr = i + dr[k]
                testc = j + dc[k]
                temp += arr[testr][testc]
            sum_arr.append(temp)
    #최댓값
    sum_max = max(sum_arr)
    print(sum_max)

