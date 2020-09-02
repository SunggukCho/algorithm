import sys; sys.stdin = open('ladder.txt', 'r')

def check(x, y):
    if x < 0 or x > 100 or y < 0 or y >= 100: return False
    if arr[x][y] ==0: return False
    return True

for tc in range(1, 11):
    case_num = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    x = y = 0

    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break

    while x:
        if dir !=2 and check(x,y-1):        #왼쪽으로 가는 경우
            y -= 1
            dir =1
        elif dir != 1 and check(x,y+1):     #오른쪽
            y += 1
            dir = 2
        else:                               #그 외, 위로 가는 경우
            x -= 1
            dir = 0
    print(y)