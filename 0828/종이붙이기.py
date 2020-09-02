#1. 재귀
def f(n):   #n: 문제의 크기
    #기저사례
    if n == 1: return 1
    if n == 2: return 3
    return f(n-1)+f(n-2)*2

for tc in range(1, int(input())+1):
    N = int(input()) // 10

    print(f(N))

#2. memoization
def f(n):   #n: 문제의 크기
    #기저사례
    if n == 1: return 1
    if n == 2: return 3

    memo[n] = f(n-1)+f(n-2)*2
    return memo[n]

for tc in range(1, int(input())+1):
    N = int(input()) // 10

    memo = [0] * (N+1)
    memo[1], memo[2] = 1, 3

    for i in range(3, N+1):
        

    print(f(N))