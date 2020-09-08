import sys; sys.stdin = open('arr.txt','r')
def find(n,s):  #n :현재 행, s : 총합
    global minV
    if n == N:  #순열을 완성하면
        #최소값인지 판단
        if s < minV :
            minV = s
        return
    elif minV <= s :    #백트래킹,
                        # 순열완성이 완성되지 않았지만 이미 최소가 아니면 종료
        return
    else:
        for i in range(N):
            if u[i] == 0 : #아직 선택되지 않았다면
                u[i] = 1
                find(n+1, s + arr[n][i])
                u[i] = 0    #선택취소

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # for row in arr:
    #     print(row)
    u = [0 for _ in range(N)]  #방문배열
    minV = 10000
    find(0,0)   #0행에서 시작, 총합 : 0
    print("#{} {}".format(tc,minV))
