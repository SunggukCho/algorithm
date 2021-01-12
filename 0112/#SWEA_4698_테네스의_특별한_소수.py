"""
핵심은 10**6까지 소수를 먼저 한 번 구해두고서, 나중에 A~B 범위 만 체크하는 것이다.
"""
N = 10**6
def set_prime():
    for i in range(N+1):
        if prime[i] == 1:
            for j in range(i*2, N+1, i):
                prime[j] = 0

prime = [1]*(N + 1)
prime[0], prime[1] = 0, 0
set_prime()

T = int(input())
for tc in range(1, T+1):
    ans = 0
    D, A, B = map(int, input().split())
    for i in range(A, B+1):
        if str(D) in str(i) and prime[i]:
            ans += 1

    print('#{} {}'.format(tc, ans))
