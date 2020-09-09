"""
3X3
1 2 3
4 5 6
7 8 9
"""
import sys
sys.stdin = open('matrix_input.txt', 'r')

#입력 1번 방법
N, M = map(int, input().split())
mylist = [0 for _ in range(N)]    # mylist = [0] * N

for i in range(N):
    mylist[i] = list(map(int, input().split()))

print(mylist)
"""
# 입력 2번 방법
N, M = map(int, input().split())
mylist = []
for i in range(N):
    mylist.append(list(map(int, input().split())))
print(mylist)

# 입력 3번 방법
N, M = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(N)]
print(mylist)

"""
for i in range(N):
    for j in range(M):
        if i < j:
            mylist[i][j], mylist[j][i] = mylist[j][i], mylist[i][j]

print(mylist)