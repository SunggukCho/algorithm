T = int(input())                     #테스트 수
for tc in range(T):
    N = int(input())                 #N x N 배열

    arr = [[0 for i in range(N)] for j in range(N)]
    # 순서 -> 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    width = len(arr)
    height = len(arr[0])

    cnt = N
    i = 1
    while True:
        # 오른쪽이 0 이면 cnt 로 변경, 오른쪽에 더 없으면 nr, nc에 추가해서 아래로 방향 선회
        nr = dr[i]
        nc = dc[i]

        if arr[nr][nc] == 0:
            arr[nr][nc] = i
            i += 1
            cnt -= 1

        if cnt == 0:
            print(arr)
            break

        if arr[nr][nc]
