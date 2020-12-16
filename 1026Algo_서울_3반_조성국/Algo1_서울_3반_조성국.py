"""
풀이
1. C의 값을 360으로 나눈 뒤 그 몫을 다시 4의 나머지로 나타낸다.
2. 나머지가 0이면 그대로, 1이면 90도, 2이면 180도, 3이면 270도 회전과 같다.
3. 90도 회전 시 행값을 그 순서대로 배열에 저장하고, 그 값들을 가장 마지막에 있는 행부터 왼쪽 열에 정렬 
4. 180도는 대칭
5. 270도는 90도가 왼쪽으로 회전
"""
def rotate(arr):
    new_arr = [[0]*K for _ in range(K)]
    for r in range(len(arr)):
        for c in range(len(arr)):   #90도 회전하는 것은 원래 배열을 열 우선순회 하는 것과 같다(순회 방향은 역순).
            new_arr[r][c] = arr[K-c-1][r]
    return new_arr

T = int(input())
for tc in range(1, T+1):
    N, C, X, Y, K, R = map(int, input().split())    # (X-1)가 열의 값, (Y-1)가 행의 값
    arr = [list(map(int, input().split())) for _ in range(N)]
    #1. arr의 일부분 떼어내기
    arr_part = []
    result = 0
    for i in range(K):
        temp = []
        for j in range(K):
            if Y-1+i < 0 or Y-1+i >= N or X-1+j < 0 or X-1+j >= N:
                result = -1
                break
            else:
                ans = arr[Y-1+i][X-1+j]
                temp.append(ans)
        arr_part.append(temp)
    if result != -1:
        #2. C각도 처리
        NC = 0
        if C > 360:
            NC = C%360
        else:
            NC = C

        if NC == 90: #1회 회전
            rotated = rotate(arr_part)
        elif NC == 180: #2회 회전
            temp = rotate(arr_part)
            rotated = rotate(temp)
        elif NC == 270: #3회 회전
            temp1 = rotate(arr_part)
            temp2 = rotate(temp1)
            rotated = rotate(temp2)
        else: #360, 0   #0회 회전
            rotated = arr_part

        #3. 원래 arr에 회전한 파트로 교체
        for i in range(K):
            for j in range(K):
                arr[Y-1+i][X-1+j] = rotated[i][j]
        #4. arr의 R번행의 값을 모두 더한다(result)
        for k in range(N):
            result+=arr[R-1][k]

    print('#{} {}'.format(tc, result))
