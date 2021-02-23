'''
BOJ_#1843방정식
https://www.acmicpc.net/problem/1843
'''
from itertools import combinations_with_replacement, combinations
def condition1(n):  #조건 1. 모두 다른 양수
    cnt = 0
    arr = [i for i in range(1, n+1)]
    comb = list(combinations(arr, 3))
    for i in comb:
        x, y, z = i[0], i[1], i[2]
        if x != y and y != z and x != z:
            if x+y == z:
                cnt += 1
    return cnt


def condition2(n):  #조건 2. 약수
    cnt = 0
    divisor = submultiple(n)
    comb = list(combinations_with_replacement(divisor, 3))
    for i in comb:
        x, y, z = i[0], i[1], i[2]
        if x+y == z:
            cnt += 1
    return cnt

def condition3(n):  #조건 3. 소수
    cnt = 0
    prime_number = []   #소수
    tmp = [False,False] + [True]*(n-1)
    for i in range(2, n+1): #소수 구하기
        if tmp[i]:
            prime_number.append(i)
            for j in range(2*i, n+1, i):
                tmp[j] = False

    comb = list(combinations(prime_number, 3))
    for i in comb:
        x, y, z = i[0], i[1], i[2]
        if x + y == z:
            cnt += 1
    return cnt


def submultiple(n): # 약수 구하는 함수
    arr = [i for i in range(1, n + 1)]
    result = []
    for i in arr:
        if n % i == 0:
            result.append(i)
    return result


N = int(input())
a = condition1(N)
b = condition2(N)
c = condition3(N)
print(a)
print(b)
print(c)
