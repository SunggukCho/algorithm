import sys; sys.stdin = open('balance.txt', 'r')
for t in range(int(input())):
    N = int(input())
    lis = list(map(int,input().split()))
    x = lis[:N]
    m = lis[N:]
    print(f'#{t+1} ',end='')
    for i in range(N-1):
        l = x[i]
        r = x[i+1]
        for _ in range(50):
            s = 0
            mid = (l+r)/2
            for k in range(i+1):
                s += m[k]/((mid-x[k])*(mid-x[k]))
            for k in range(i+1,N):
                s -= m[k]/((mid-x[k])*(mid-x[k]))
            if s > 0:
                l = mid
            else:
                ans = mid
                r = mid
                #print(mid)
        print('%.10f' % ans )
