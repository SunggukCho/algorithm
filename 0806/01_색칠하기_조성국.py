import sys
sys.stdin = open('color.txt', 'r', encoding = 'utf-8')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    arr = [[0 for _ in range(10)] for _ in range(10)]    #10x10 배열에 0 넣고 시작

    '''
    풀이접근: 10X10배열에 0을 넣고, 빨간색의 경우 +1, 파란새의 경우 +2를 해준다
    이때, 빨간색과 파란색이 겹치는 보라색 부분은 +1+2 , 즉 +3이 되는 경우이므로 이 +3을 카운트 한다.
    '''

    for i in M:
        start_r = i[0] #2                               #시작 x좌표
        start_c = i[1] #2                               #시작 Y좌표
        end_r = i[2] #4                                 #끝 x좌표
        end_c = i[3] #4                                 #끝 y좌표

        if i[-1] == 1:                                  #빨간색이면 1추가
            for j in range(end_r - start_r+1):
                for k in range(end_c-start_c+1):
                    arr[start_r+j][start_c+k] += 1
        else:                                           #파란색이면 2추가
            for j in range(end_r - start_r+1):
                for k in range(end_c-start_c+1):
                    arr[start_r+j][start_c+k] += 2

    cnt = 0                                            #보라색은 3인 영역이므로 3의 개수 카운트
    for l in arr:
        for m in l:
           if m == 3:
               cnt += 1
    print('#{} {}'.format(tc, cnt))