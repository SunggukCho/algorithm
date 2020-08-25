import sys
sys.stdin = open('palindrome2.txt', 'r')

# def palindrome(arr):
#     if len(arr) < 2:
#         return True
#     if arr[0] != arr[-1]:
#         return False
#     return palindrome(arr[1:-1])

def palindrome(arr):
    arr = arr
    arr_rev = arr[::-1]
    if arr == arr_rev:
        return 1
    else:
        return 0

T = int(input())
for tc in (1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(100)]

    M = 100
    max_len = []
    #가로 서치
    for i in range(M):
        for j in range(M):                          #왼쪽에서 압박수사
            for k in range(M):                      #오른쪽에서 한 칸씩 줄어들면서 압박수사
                new_arr = arr[i][j:M-k]
                if palindrome(new_arr):
                    max_len.append(len(new_arr))
                    break

    #세로 서치
    column = []
    for i in range(M):
        temp = []
        for j in range(M):
            temp.append(arr[j][i])
        column.append(temp)

    for i in range(M):
        for j in range(M):  # 왼쪽에서 압박수사
            for k in range(M):  # 오른쪽에서 한 칸씩 줄어들면서 압박수사
                new_arr = column[i][j:M-k]
                if palindrome(new_arr):
                    max_len.append(len(new_arr))
                    break
    result = max(max_len)
    print('#{} {}'.format(N, result))
