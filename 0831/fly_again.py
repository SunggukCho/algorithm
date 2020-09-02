import sys; sys.stdin = open('fly_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            ans = 0
            for r in range(M):
                for c in range(M):
                    ans += arr[i+r][j+c]

            ans_list.append(ans)
        ans_list.append(ans)

    result = max(ans_list)
    print('#{} {}'.format(tc, result))