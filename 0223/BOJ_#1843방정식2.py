'''
BOJ_#1843방정식
https://www.acmicpc.net/problem/1843
'''
from itertools import combinations_with_replacement

N = int(input())
arr = [i for i in range(1, N + 1)]

divisor = [] #약수
for i in arr:
    if N % i == 0:
        divisor.append(i)

prime_number = []   #소수
tmp = [False,False] + [True]*(N-1)
for i in range(2, N+1): #소수 구하기
    if tmp[i]:
        prime_number.append(i)
        for j in range(2*i, N+1, i):
            tmp[j] = False

cond1 = 0
cond2 = 0
cond3 = 0

comb = list(combinations_with_replacement(arr, 3))
for k in comb:
    x, y, z = k[0], k[1], k[2]
    if x+y == z:    #일단 공통 조건 만족
        if x != y and x != z and y != z:
            cond1 += 1
        if x in divisor and y in divisor and z in divisor:
            cond2 += 1
        if x in prime_number and y in prime_number and z in prime_number:
            cond3 += 1
print(cond1)
print(cond2)
print(cond3)
