import sys; sys.stdin = open('russia.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    W = [0] * N
    B = [0] * N
    R = [0] * N

    for i in range(len(arr)):
        w_cnt = arr[i].count('W')
        b_cnt = arr[i].count('B')
        r_cnt = arr[i].count('R')
        W[i] = w_cnt
        B[i] = b_cnt
        R[i] = r_cnt

    #깃발 누적합
    for i in range(1, N):
        W[i] += W[i-1]
        B[i] += B[i-1]
        R[i] += R[i-1]
    ans = N*M
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = M*(i+1) - W[i]
            cnt += M*(j-i)-(B[j]-B[i])
            cnt += M*(N-1 - j) - (R[N-1]-R[j])
            ans = min(ans, cnt)
    print('#{} {}'.format(tc, ans))
