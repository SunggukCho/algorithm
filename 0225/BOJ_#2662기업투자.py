'''
BOJ_#2662기업투자
https://www.acmicpc.net/problem/2662

4 2
1 5 1
2 6 5
3 7 9
4 10 15
'''

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

table = [[0]*M for _ in range(N)]   #최대값 table
invest = [[0]*M for _ in range(N)]    #회사별 투자 금액

for k in range(N):
    table[k][0] = arr[k][0]


for i in range(N):
    for j in range(1, M):
        table[i][j] = max(arr[i][j], table[i][j-1])
