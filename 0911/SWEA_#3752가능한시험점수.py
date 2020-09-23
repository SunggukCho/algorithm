"""
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bit = [0] * N
    arr = list(map(int, input().split()))

    result = [0]
    for i in arr:
        result2 = result[:]
        for j in result2:
            temp = i+j
            if temp not in result:
                result.append(temp)

    print('#{} {}'.format(tc, len(result)))
