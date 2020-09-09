import sys
sys.stdin = open('special.txt', 'r')
"""
# 1번 min/max 함수 써보기
T = int(input())
for i in range(1, T+1):
    size = int(input())                           #데이터 갯수
    numbers = list(map(int, input().split()))     #숫자 대소 비교 대상
    minimum = min(numbers)                        #최소 구하기
    maximum = max(numbers)                        #최대 구하기
    result = maximum - minimum                    #결과 = 최대 - 최소

    print('#{} {}'.format(i, result))


# 2번 min/max 함수 안 써보기
T = int(input())
for i in range(1, T+1):
    size = int(input())                           #데이터 갯수
    numbers = list(map(int, input().split()))     #숫자 대소 비교 대상

    numbers.sort()                                #numbers 소팅
    minimum = numbers[0]                          #minimum = numbers인덱스의 첫 번째 값
    maximum = numbers[-1]                         #maximum = numbers인덱스의 끝 값
    result = maximum - minimum

    print('#{} {}'.format(i, result))
"""
# 3번, min / max 함수 만들어서 쓰기
def find(a, n):
    max_value =  0  #극 최소값 0 (양수범위)
    min_value =  999999  #극 최대값 9999999
    for i in range(1, n):
        if a[i] >= max_value:
            max_value = a[i]
        if a[i] < min_value:
            min_value = a[i]
    return max_value-min_value
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    v = list(map(int, input().split()))
    print("#{} {}".format(tc, find(v,N)))
