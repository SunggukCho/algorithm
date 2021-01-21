import sys; sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    Str = input()
    arr = []
    for i in range(len(Str)):
        arr.append(Str[i:])
    arr.sort()
    ans = arr[K-1]
    print('#{} {}'.format(tc, ans))
