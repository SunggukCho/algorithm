import sys
sys.stdin = open('GNS_test_input.txt')

new_order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
new_order_dict = {}
#{"ZRO": 0, "ONE": 1, ... 과 같은 Dictionary 생성}
for i in range(len(new_order)):
    d1 = {new_order[i]:i}
    new_order_dict.update(d1)

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(str, input().split()))
    arr = list(map(str, input().split()))
    M = int(M)

    #arr = [['ZRO',0], ...]과 같은 list만들기
    for i in range(len(arr)):
        key = arr[i]
        value = new_order_dict[key]
        arr[i] = key, value
        
    new_arr = []
    new_arr = sorted(arr, key=lambda arr: arr[1])   #새로운 리스트에 arr[1](숫자)값을 기준으로 정렬
    result = ''
    for i in new_arr:
        result += ' ' + i[0]

    result = result[1:]
    print('#{} \n{}'.format(tc, result))
