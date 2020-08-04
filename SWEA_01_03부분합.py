import sys
sys.stdin = open('sample_input_sum.txt', 'r')                      #파일로 input받기


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

