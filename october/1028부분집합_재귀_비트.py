# 부분집합 - 1. bit
arr = [1,2,3]
N = len(arr)
# bit = [0]*N
def powerset(arr):
    for i in range(1 << N):       #i: 0 ~ 7
        for j in range(N):
            if i & (1 << j):        # 1<<j -> 1, 2, 4
                print(arr[j], end=' ')
        print()
powerset(arr)
"""
simulation
i:0 , j=0, i&(1<<j) = 0이라 아무일도 안일어남
i:0, j=1 F
i:0, j=2 F
i:1, j=0 T, i&(1<<j) = 1 -> arr[j(=0)] -> arr[0]인 1이 출력
i:1, j=1 F
i:1, j=2 F
i:2, j=0 F
i:2, j=1 T, i&(1<<j) = 1, arr[j(=1)] -> arr[1]인 2 출력 
i:2, j=2 F, 
i:3, j=0 T, i&(1<<j) = 1, arr[j(=0)] -> arr[1]인 1 출력
i:3, j=1 T, i&(1<<j) = 2, arr[j(=1)] -> arr[1]인 2 출력
i:3, j=2 F, 
...
"""

# 2. 부분집합 - 2. 재귀
# def powerset(k):
#     if N == k:
#         for i in range(N):
#             if B[i] == 1:
#                 print(arr[i], end=' ')
#         print()
#     else:
#         B[k] = 0
#         powerset(k+1)
#         B[k] = 1
#         powerset(k+1)
#
# B = [0]*N
# powerset(0)
#

