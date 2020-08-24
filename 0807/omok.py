import sys
sys.stdin = open('omok.txt', 'r')

arr = []
new_arr = [[0 for _ in range(19)] for _ in range(19)]

T = 19
for tc in range(1, T+1):
    arr2 = list(map(int, input().split()))
    arr.append(arr2)

def answer():
    #1. 행 우선순회
    for i in range(14):
        for j in range(14):
            if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == arr[i][j+4] == 1:
                if arr[i][j] != arr[i][j+5]:
                    return(1, i+1, j+1)
                else:
                    return None
            elif arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == arr[i][j+4] == 2:
                if arr[i][j] != arr[i][j+5]:
                    return(2, i+1, j+1)
                else:
                    return None

    #2. 열 우선순회
    for i in range(14):
        for j in range(14):
            if arr[i][j] == arr[i+1][j] == arr[i+2][j] == arr[i+3][j] == arr[i+4][j] == 1:
                if arr[i][j] != arr[i+5][j]:
                    return (1, i + 1, j + 1)
                else:
                    return None
            elif arr[i][j] == arr[i+1][j] == arr[i+2][j] == arr[i+3][j] == arr[i+4][j] == 2:
                if arr[i][j] != arr[i + 5][j]:
                    return(2, i+1, j+1)
                else:
                    return None

    # #3. 격자 순회
    for i in range(0, 14):
        for j in range(0, 14):
            if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4] == 1:
                if arr[i][j] != arr[i+5][j+5]:
                    return(1, i+1, j+1)
                else:
                    return None
            elif arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4] == 2:
                if arr[i][j] != arr[i+5][j+5]:
                    return(2, i+1, j+1)
                else:
                    return None

result = answer()

if result is not None:
    print('{}\n{} {}'.format(result[0], result[1], result[2]))
else:
    print(0)