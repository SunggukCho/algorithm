# arr = ['A','B','C']
# n = 3
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end=' ')
#     print()
"""
0000
0001
0010
0011
0100
0101
0110
0111
"""
rests = [1, 2, 3, 4, 5, 6]
for i in range(6):
    print(rests.pop(0))