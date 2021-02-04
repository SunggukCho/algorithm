'''
https://www.acmicpc.net/problem/2563
풀이
100x100 도화지 준비
10x10 정사각형 모양에 1넣고 끝나면 총합 
'''
N = int(input())
sheets = [list(map(int, input().split())) for _ in range(N)]
#sheets[i][0] => x좌표
#sheets[i][1] => y좌표
MAP = [[0]*100 for _ in range(100)]
while len(sheets):
    x, y = sheets.pop(0)
    for i in range(10):
        for j in range(10):
            MAP[y+i][x+j] = 1

result = 0
for row in MAP:
    result += sum(row)
print(result)
