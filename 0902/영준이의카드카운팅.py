import sys; sys.stdin = open('card.txt','r')

T = int(input())
for tc in range(1, T+1):
    cards = input()

    deck = []
    for i in range(0, len(cards), 3):
        deck.append(cards[i:i+3])

    S, D, H, C = 13, 13, 13, 13
    visit = []
    check_error = 0
    #deck순회하면서 같은 값이 있으면 'error'출력. visit 사용
    for i in range(len(deck)):
        if deck[i] not in visit:
            visit.append(deck[i])
            if 'S' in deck[i]:
                S -= 1
            elif 'D' in deck[i]:
                D -= 1
            elif 'H' in deck[i]:
                H -= 1
            elif 'C' in deck[i]:
                C -= 1
        else:
            check_error += 1
            break
    if check_error == 0:
        print('#{} {} {} {} {}'.format(tc, S, D, H, C))
    else:
        print('#{} {}'.format(tc, 'ERROR'))
