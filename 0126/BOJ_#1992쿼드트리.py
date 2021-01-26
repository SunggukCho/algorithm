'''
풀이
재귀!
8
00000000
00000000
00001111
00001111
00011111
00111111
00111111
00111111

반례1
4
0000
0000
0000
0000

반례2
4
0101
0000
0101
0000

-> 답: ((0100)(0100)(0100)(0100))
나의 이전 코드는 (0100) 출력 해서 계속 틀렸다.
'''
import sys; sys.setrecursionlimit(1000000)

def quad(x, y, n):
    if n == 1:
        return str(arr[x][y])
    else:
        half = n // 2

        left_up = quad(x, y, half)
        right_up = quad(x, y+half, half)
        left_down = quad(x+half, y, half)
        right_down = quad(x+half, y+half, half)

        if left_up == right_up == left_down == right_down and len(str(left_up))==1:
            return str(left_up)
        return "(" + str(left_up) + str(right_up) + str(left_down) + str(right_down) + ")"


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

ans = quad(0, 0, N)
print(str(ans))
