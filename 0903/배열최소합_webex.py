import sys; sys.stdin = open('arr.txt','r')

def find(n, s):
    global minV
    if n == N:
        #순열에 해당하는 값을 더하고, 최소값인지 판단
        if s < minV:
            minV = s
        return
    else:
        for i in range(N):
            #방문했던 곳이냐?
            if u[i] == 0:
                u[i] = 1
            #아니면 값 가져오고 (재귀함수 호출)
                find(n+1,s+arr[n][i])
            #다시 돌아올 수 있도록 방문했다고 표시한거 지우기
                u[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    u = [0 for _ in range(N)]                                   # 방문배열

    minV = 10000    #가상의 최소값. 일단 큰 수로 지름
    ans = find(0,0)       #현재 행, 총합 (0행에서 시작, 총합 0)
    print(minV)

