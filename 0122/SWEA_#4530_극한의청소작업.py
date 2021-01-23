'''
3
-1 1
-5 3
-123123123123 789789789789
'''
def toNine(n, n_len):
    ans = 0
    arr = list(str(n))
    for i in range(n_len):
        j = n_len-i-1
        ans += int(arr[i])*9**j
        print(ans)
    return ans

# T = int(input())
# for tc in range(1, T+1):
#     A, B = map(int, input().split())
#
#
#     result = 0
#
#     if A > 0:
#         len_A = len(str(A))
#         len_B = len(str(B))
#         a = toNine(A, len_A)
#         b = toNine(B, len_B)
#         result = b-a
#     else:
#         len_A = len(str(-A))
#         len_B = len(str(B))
#         if B > 0:
#             b = toNine(B, len_B)
#             a = toNine(-A, len_A)
#
#     print('#{} {}'.format(tc, result))
