import sys; sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    #K개의 빈 칸이 연속으로 나오면 row +=1
    #가로순회
    for i in range(N):
        row = 0
        for j in range(N):
            if arr[i][j] == 1:  #연속으로 나올 때는 row를 올려줌
                row += 1
            else:               #연속이 끊겼을 때는 result에 append해주고 row를 0으로 초기화
                if row != 0: result.append(row)
                row = 0
        if row != 0: result.append(row) #순회가 끝나고 혹시나 row에 0이 아닌 값이 남아 있을 경우 result에 append
    #세로순회
    for i in range(N):
        col = 0
        for j in range(N):
            if arr[j][i] == 1:
                col += 1
            else:
                if col != 0: result.append(col)
                col = 0
        if col != 0: result.append(col)

    ans = result.count(K)
    print('#{} {}'.format(tc,ans))