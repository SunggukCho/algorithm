import sys; sys.stdin = open('balance.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    x_axis = arr[0:N]
    mass = arr[N:]

    #F = G * m1 * m2 / (d * d),