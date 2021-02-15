'''
BOJ_#1655가운데를말해요 - 오답
https://www.acmicpc.net/problem/1655
여지없이 시간초과

7
1
5
2
10
-99
7
5
'''
T = int(input())
arr = []
for tc in range(1, T+1):
    N = int(input())
    arr.append(N)
    arr.sort()
    if tc % 2 == 0: #짝수
        idx = tc // 2
        ans = arr[idx-1]
    else:
        idx = tc // 2
        ans = arr[idx]
    print(ans)