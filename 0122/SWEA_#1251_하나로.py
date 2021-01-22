'''
# prim / kruskal / MST 학습 후 재도전
2
2
0 0
0 100
1.0
4
0 0 400 400
0 100 0 100
1.0
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    print(N, X, Y, E)