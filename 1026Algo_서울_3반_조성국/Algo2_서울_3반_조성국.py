"""
풀이
(전체의 합) - (뛰어 넘는 칸의 합)
arr의 index값들이 1차이가 나지 않는 것들 중에서 최소값을 구하고 arr의 전체 합에서 빼주면 최대값이 나온다.
"""
from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    K = N-M                         #뛰어 넘는 칸의 개수
    A = [i for i in range(0, N)]    #인덱스만을 구하기 위한 arr의 length와 같은 크기의 배열

    comb = list(combinations(A, K)) #N-M의 크기 만큼의 부분집합의 개수 구하기
    candidates = []                 #index값이 최소 1을 초과하는 것들만 후보군(candidates)가 될 수 있음
    for i in comb:
        for j in range(len(i)-1):
            if abs(i[j]-i[j+1]) <= 1:
                break
            else:
                if i[j]-i[j+1]:
                    candidates.append(i)
    #후보군 중에서 arr의 값들의 합을 구하고 가장 최소인 값을 sum_min으로 넣어준다.
    sum_min = 9999
    for i in candidates:
        temp = 0
        for j in range(len(i)):
            temp+=arr[i[j]]
        if sum_min > temp:
            sum_min = temp
    #답(ans) = arr의 합 - 최소값
    ans = sum(arr)-sum_min

    print('#{} {}'.format(tc, ans))
