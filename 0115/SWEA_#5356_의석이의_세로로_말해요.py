"""
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx
"""
T = int(input())
for tc in range(1, T+1):
    # arr = [list(map(str, input())) for _ in range(5)]
    arr = []
    N = 0
    for _ in range(5):
        new_input = list(map(str, input()))
        arr.append(new_input)
        if len(new_input) > N:
            N = len(new_input)

    for i in arr:
        if len(i) < N:
            empty = N-len(i)
            for j in range(empty):
                i.append('')

    ans = ''
    for i in range(N):
        for j in range(5):
            ans += arr[j][i]
    print('#{} {}'.format(tc, ans))
