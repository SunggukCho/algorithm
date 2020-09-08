import sys; sys.stdin=open('회전.txt','r')
def turn(arr):
    start = arr.pop(0)
    arr.append(start)
    return arr

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(0, M+1):
        if i == M:
            print('#{} {}'.format(tc, result))
            break
        else:
            ans = turn(arr)
            result = ans[0]
