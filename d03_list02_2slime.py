T = int(input())                     #테스트 수
for tc in range(T):
    N = int(input())                 #N x N 배열

    arr = [[0 for i in range(N)] for i in range(N)]
    # 순서 -> 우, 하, 좌, 상
    u = -1
    d = 1
    r = 1
    l = -1


    for j in range(N):
        if j+1 != len(arr):
            arr[j] = j+1
            l += 1
        else:
            arr[j] = j|1