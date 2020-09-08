"""
풀이접근
1. 2일때, 모든 열에 대해 검사 위에서 아래로
2.내려오면서 1을 만났을 때는: 교착상태
3. 내려오면서 1을 못만났을 때: 교착상태 X
4. 1일 때, 방해물임을 표시
"""
import sys; sys.stdin = open('magnet.txt','r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0                                     #교착상태 수
    for c in range(N):                          #열방향순회
        obstacle = 0                            #방해물 저장
        for r in range(N):                      #세로 방향 순회
            if arr[r][c]==0: continue           #자성체 없으면 넘어가라
            elif arr[r][c]==2 and obstacle == 0:#S극인데 이제까지 방해물 없었으면 넘어가라
                continue
            elif arr[r][c]==2 and obstacle != 0:#S극인데 이제까지 방해물인 N극을 만났을 때 : 교착상태
                cnt += 1                        #교착상태 수 누적합
                obstacle = 0                    #2를 만난 순간 1의 갯수와는 상관없이 다 교착상태가 됨. 방해물 한 번 셌으면 없애주자
            elif arr[r][c] == 1:
                obstacle = 1
    print('#{} {}'.format(tc, cnt))
