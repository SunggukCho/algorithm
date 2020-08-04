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