"""
색종이의 넓이를 구하는 방법에 대한 아이디어가 중요한 문제
겹치는 부분만 구하려고 하면 생각보다 매우 귀찮음.
차라리 100x100짜리 판을 만들어두고 모두 10의 크기인 정사각형이므로 반복문을 돌면서 변으로부터의 길이가 10이내인 점을 모두 1로 표기함.
이후 그 1의 값을 모두 합하면 정답이 나온다.
"""
T = int(input())

arr = [list(map(int, input().split())) for _ in range(T)]
G = [[0]*101 for _ in range(101)]
ans = 0
for i in range(T):
    x, y = arr[i][0], arr[i][1]
    for j in range(10):
        for k in range(10):
            if G[x+j][y+k] == 0:
                G[x+j][y+k] = 1
                ans += 1
            else:
                continue
print(ans)
