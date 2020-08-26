import sys
sys.stdin = open('palindrome.txt', 'r')

def palindrome(N, M, arr):
    result = 0                  #cnt 식별자
    for i in range(N):          #가로방향 palindrome 서치
        for j in range(N):
            m = M//2            #M//2 몫
            for l in range(N-M+1):
                for k in range(m):
                    if arr[i][k+l] == arr[i][N-k-1]:
                        result += 1
                        continue
                    else:
                        result = 0
                        break
                if result >= m:
                    row_arr = []
                    if N == M:
                        for r in range(M):
                            row_arr.append(arr[i][j+r])
                    else:
                        for r in range(M):
                            row_arr.append(arr[i][j+m+r+1])
                    return row_arr

    result = 0                  # cnt 식별자
    for i in range(N):          # 세로방향 palindrome 서치
        for j in range(N):
            m = M // 2          # N//2 몫
            for l in range(N-M+1):
                for k in range(m):
                    if arr[k+l][j] == arr[N-k-1][j]:
                        result += 1
                        continue
                    else:
                        result = 0
                        break
                if result >= m:
                    column_arr =[]
                    if N == M:
                        for c in range(N):
                            column_arr.append(arr[c][j])
                    else:
                        for c in range(N):
                            column_arr.append(arr[c+m+i+1][j])
                    return column_arr

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ans = palindrome(N, M, arr)
    result = ''
    for i in ans:
        result += i
    print('#{} {}'.format(tc, result))
