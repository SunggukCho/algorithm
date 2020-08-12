import sys
sys.stdin = open('fly.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    #변수 입력
    N, M = map(int, input().split())
    #N :행, 열의 길이, M: 파리채 크기
    arr = []

    for i in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)

    sum_arr = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp= []
            for k in range(M):
                for l in range(M):
                    temp.append(arr[i + k][j + l])
            sum_arr.append(sum(temp))

    max_i = max(sum_arr)
    print('#{} {}'.format(tc, max_i))