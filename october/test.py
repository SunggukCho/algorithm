#1. shift 연산

arr = [1,2,3,4]

# def powerset(n):
#     x = len(n)
#     for i in range(1 << x):
#         print([n[j] for j in range(x) if (i & (1 << j))])
# print(powerset(arr))

#2. combinations import
from itertools import combinations
#
# a = [1, 2, 3]
# result = []
#
# for i in range(0, len(a)+1):
#     c = combinations(a, i)
#     result.extend(c)
#
# print(result)

#3. 재귀
N = len(arr)
A = [0]*N
def powerset(k):
    if N == k:
        print(A)
    else:
        A[k] = 0
        powerset(k+1)
        A[k] = 1
        powerset(k+1)
#powerset(0)
print(list(combinations(arr,2)))