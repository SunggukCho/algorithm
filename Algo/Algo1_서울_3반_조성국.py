"""
3
3 3 3
1 2 3
4 5 6
7 8 9
4 4 3
2 3 4 3
5 6 7 8
9 7 9 7
1 2 4 5
6 5 4
11 75 97 9 36
14 33 72 12 57
44 77 38 98 67
38 30 69 16 48
45 29 35 64 56
23 75 48 87 45
"""
"""
풀이접근
1. 가로(M)-K, 세로(N)-K의 범위에서 이중 for 문을 돌면서 K크기 사각형 내부의 합을 모두 구한다.
2.  K크기 사각형 내부를 구하기 위해 K-2 크기의 사각형의 합을 구한 뒤 뺀다.
3. 사각형의 합을 배열에 넣고 MAX와 MIN을 구한 뒤 MAX-MIN한다.
"""
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    results = []
    for i in range(N - K + 1):  # 큰 사각형 범위
        for j in range(M - K + 1):  # 큰 사각형 범위
            large = 0  # 큰 사각형의 총합
            small = 0  # 작은 사각형의 총합
            for k in range(K):
                for l in range(K):
                    large += arr[k + i][l + j]
            for m in range(K - 2):  # 작은 사각형의 크기는 K에서 양변을 하나씩 빼서 K-2
                for n in range(K - 2):
                    small += arr[i + m + 1][j + n + 1]
            ans = large - small  # 큰 사각형 - 작은 사각형
            results.append(ans)

    result = max(results) - min(results)
    print('#{} {}'.format(tc, result))
