import sys
sys.stdin = open('palindrome.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    #가로 체크
    cnt = 0
    for i in range(N):
        for j in range(N-M+1):
            row = arr[i][j:j+M]
            row_reverse = row[::-1]
            if row == row_reverse:
                result = ''
                for k in row:
                    result += k
                if len(result)>= 1:
                    cnt += 1
                print('#{} {}'.format(tc, result))

    #세로체크
    if cnt <= 0:
        for i in range(N-M+1):
            for j in range(N):
                column = []
                for k in range(M):
                    column.append(arr[i+k][j])
                column_reverse = column[::-1]
                if column == column_reverse:
                    ans = ''
                    for l in column:
                        ans += l
                    print('#{} {}'.format(tc, ans))
