arr = [
    [1,2,3,4],
    [5,6,7,8]
    [9,10,11,12]
]

#행우선 순회
N = len(arr)        #행의 길이
M = len(arr[0])     #열의 길이

for i in range(N):
    for j in range(M):
        print(arr[i][j], end = ' ')
    print()

#열우선 순회
for j in range(M):
    for i in range(N):
        print(arr[i][j], end = ' ')
    print()

#지그재그 순회

for i in range(N):
    #짝수행일 때는 똑같이
    if i % 2 == 0:
        for j in range(M):
            print(arr[i][j], end = ' ')
        print()

    #홀수행
    else:
        for j in range(M-1, -1, -1):
            print(arr[i][j], end = ' ')
        print()