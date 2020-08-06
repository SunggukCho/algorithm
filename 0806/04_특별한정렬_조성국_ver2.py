import sys
sys.stdin = open('special.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    