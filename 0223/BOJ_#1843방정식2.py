'''
BOJ_#1843방정식
https://www.acmicpc.net/problem/1843
'''
from itertools import combinations_with_replacement

N = int(input())

arr = [i for i in range(1, N + 1)]  #약수
result = []
for i in arr:
    if N % i == 0:
        result.append(i)

prime_number = []   #소수
tmp = [False,False] + [True]*(N-1)
for i in range(2, N+1): #소수 구하기
    if tmp[i]:
        prime_number.append(i)
        for j in range(2*i, N+1, i):
            tmp[j] = False

