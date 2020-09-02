import sys; sys.stdin = open('arr.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N

    ans = []
    for i in range(N):
        start = arr[0][i]