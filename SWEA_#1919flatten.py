import sys
sys.stdin = open('input_flatten.txt', 'r')                      #파일로 input받기

T = 10
for tc in range(1, T + 1):
    num = int(input())
    box = list(map(int, input().split()))

    for i in range(num):
        minimum = min(box)                 #box의 최솟값
        min_idx = box.index(minimum)       #box 최솟값의 인덱스
        maximum = max(box)                 #box의 최댓값
        max_idx = box.index(maximum)       #box 최댓값의 인덱스

        #dump 작업
        maximum -= 1                       #max값에서 -1
        minimum += 1                       #min 값에서 +1

        box[min_idx] = minimum             #바뀐 min값을 box에 넣어줌
        box[max_idx] = maximum             #바뀐 max값을 box에 넣어줌

        result = max(box) - min(box)       #덤프 후 result


        if i == num-1:
            print('#{} {}'.format(tc, result))
        i += 1
