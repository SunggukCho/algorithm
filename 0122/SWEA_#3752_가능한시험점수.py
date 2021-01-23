'''
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1
'''

from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    result = set()
    result.add(0)
    for score in scores:
        temp = list(result)
        for n in temp:
            result.add(score + n)
    print('#{} {}'.format(tc, len(result)))
