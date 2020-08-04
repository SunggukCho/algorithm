import copy
import sys
sys.stdin = open('sample_input_bus.txt', 'r')                      #파일로 input받기

T = int(input())
for tc in range(1, T+1):
    #입력
    data = list(map(int, input().split()))
    loc_M = list(map(int, input().split()))

    #할당
    K = data[0]      #충전 후 최대 거리
    N = data[1]      #정류장 수
    M = data[2]      #충전기가 있는 정류장 수
    loc_M            #충전소 위치 [1, 3, 5, 7, 9]

    energy = K
    cnt = 0
    temp = []

    for i in range(1, N):
        if i in loc_M:
            if energy < K:
                energy = K
                cnt += 1
            else:
                energy -= 1
        else:
            energy -= 1
        if energy <= 0:
            cnt = 0
            break

    print(cnt)
