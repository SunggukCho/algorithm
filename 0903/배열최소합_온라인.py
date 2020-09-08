import sys; sys.stdin = open('arr.txt','r')
#1. 순열 모두 구하기 -> 이렇게 하면 시간 초과난다.
def perm(k):
    if k == N:
        S = 0
        for r, c in enumerate(cols):
            S += arr[r][c]
        global ans
        ans = min(ans, S)

    for i in range(k, N):
        cols[k], cols[i] = cols[i], cols[k]
        perm(k+1)
        cols[k], cols[i] = cols[i], cols[k]

#2. 가지치기를 해보자
def perm2(k, cur_sum):
    if k == N:
        S = 0
        for r, c in enumerate(cols):
            S += arr[r][c]
        global ans
        ans = min(ans, S)

    for i in range(k, N):
        cols[k], cols[i] = cols[i], cols[k]
        perm(k+1, cur_sum+arr[k][cols[k]])
        cols[k], cols[i] = cols[i], cols[k]

#3. 수정 최종
def perm3(k, cur_sum):
    global ans
    #만약 탐색도중 지금까지의 합이 이전 최소값보다 크면 굳이 더 갈 필요 없으므로 멈춘다.
    if ans <= cur_sum: return
    if k == N:
        ans = min(ans, S)

    for i in range(k, N):
        cols[k], cols[i] = cols[i], cols[k]
        perm(k+1, cur_sum+arr[k][cols[k]])
        cols[k], cols[i] = cols[i], cols[k]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cols = [i for i in range(N)]
    ans = 99999
    perm(0)
    print(ans)
