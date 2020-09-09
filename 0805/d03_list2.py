import sys
sys.stdin = open('d03_list2_input.txt', 'r')

for i in range(10):
    N = int(input())
    temp = []
    M = [list(map(int, input().split())) for _ in range(100)]   #100x100 덩어리 한 개

    arr_r = []      #행 합을 모아두는 배열
    arr_c = []      #열 합을 모아두는 배열
    arr_x = []      #대각선 우하향 합을 모아두는 배열
    arr_y = []      #대각선 우상향 합을 모아두는 배열
    #1. 행
    for j in range(100):
        sum_r = 0
        for k in M[j]:
            sum_r += k
        arr_r.append(sum_r)
    #2. 열
    for j in range(100):
        sum_c = 0
        for k in M:
            sum_c += k[j]
        arr_c.append(sum_c)

    #3. 대각 우하향
    for j in range(100):
        sum_x = 0
        for k in M:
            idx = M.index(k)     #M을 돌면서 index값이 k인 값들만 선별
            sum_x +=k[idx]
        arr_x.append(sum_x)

    #4. 대각 우상향
    for j in range(100):
        sum_y = 0
        for k in M:
            idx = M.index(k)
            idx_y = abs(len(k)-idx-1)
            sum_y += k[idx_y]
            sum_y
        arr_y.append(sum_y)
    arr = arr_r + arr_c + arr_x + arr_y     #행, 열, 대각선 최댓값을 담고 있는 arr 통합
    result = max(arr)                       #그 중 최대값을 result에 반환
    print('#{} {}'.format(i+1, result))