# T = 1
# size = 9 8
# A = 7 4 2 0 0 6 0 7 0

### 강사님 풀이
"""
#이중 리스트 문제
상자를 채울 배열 room준비
각 행에서 가장 높은 박스 위치를 배열 boxTop에 저장

"""
T = int(input())
for tc in range(1, T+1):
    #input
    N, M = map(int, input().split())
    boxTop = list(map(int, input().split()))
    room = [[0 for _ in range(M)] for _ in range(N)]    #안쓰는 변수 "_"사용 가능
    for i in range(N):
        for j in range(boxTop[i]):
            room[i][j] = 1

    for row in room:
        print(row)
    #calc
    max = 0  #최대 낙차 계산

    for i in range(N):
        if boxTop[i] > 0:     #상자가 있다면
            dist = 0
            for j in range(i+1, N): #상자 위치 한 칸 다음부터 마지막까지 반복
                if room[j][boxTop[i]-1] == 0:
                    dist += 1     #개수 카운팅
            if max < dist:
                max = dist

    #output
    print(max)