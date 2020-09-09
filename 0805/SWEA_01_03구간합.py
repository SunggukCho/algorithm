import sys
sys.stdin = open('sample_input_sum.txt', 'r')               #파일로 input받기
"""
T = int(input())
for tc in range(1, T+1):
    #입력
    size = list(map(int, input().split()))
    data = list(map(int, input().split()))

    loop = size[1]
    len_data = len(data)

    maximum= int()
    minimum= int()
    temp = []
    num = 0
    for i in range(len_data-loop+1):
        for j in range(i,i+loop):
            num += data[j]
        temp.append(num)
        num = 0

    minimum = min(temp)
    maximum = max(temp)

    result = maximum - minimum
    print('#{} {}'.format(tc, result))
"""
#새로운 풀이. 하나 빼고, 하나만 더하기
T = int(input())
for tc in range(1, T+1):
    size = list(map(int, input().split()))
    data = list(map(int, input().split()))

    N = size[0]
    M = size[1]

    sum_arr = []
    for i in range(N-M+1):
        sum_subset = 0
        for j in range(M):
            sum_subset += data[i+j]

        sum_arr.append(sum_subset)


