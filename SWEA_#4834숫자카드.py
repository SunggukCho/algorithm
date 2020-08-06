import sys
sys.stdin = open('sample_input_card.txt', 'r')                      #파일로 input받기

T = int(input())
for tc in range(1, T+1):
    #입력
    card_num = list(map(int, input().split()))
    cards_str = list(input())
    cards = list(map(int, cards_str))

    cards.sort(reverse=True) #나중에 같은 value일 경우 큰 값이 나오도록 reverse sort

    cards_dict = {}          #count해서 key에 숫자, value에 count 숫자를 넣음
    for i in cards:
        cards_dict.update({i:cards.count(i)})

    def f1(x):               #value로 key값 알아내기
        return cards_dict[x]

    key_max = max(cards_dict.keys(), key=f1)

    print('#{} {} {}'.format(tc, key_max, cards_dict[key_max]))
    
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr[0] * 10        #10칸짜리 배열 선언 0으로 초기화 -> 숫자 카운팅 용도
    num = [int(n) for n in input()] 
    
    for n in num:
        arr[n] = arr[n]+1    #arr배열의 n번 인덱스의 데이터를 하나 증가
        
    max_idx = 0         #최댓값의 위치를 저장
    for i in range(len(arr)):
        if arr[max_idx] < arr[i]:
            max_idx = i
        iff arr[max_idx] == arr[i] and max_idx < i:
        max_idx = i