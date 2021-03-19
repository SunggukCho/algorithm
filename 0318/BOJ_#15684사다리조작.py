'''
BOJ_#15684사다리조작
https://www.acmicpc.net/problem/15684

2 0 3
-> 0

2 1 3
1 1
-> 1
'''

N, M, H = map(int, input().split()) #세로선, 가로선, 다리 갯수
arr = [[0]*N for _ in range()]
result = 0 # M이 0인 경우 최종 답은 0
if M != 0:
    i, j = map(int, input().split())




