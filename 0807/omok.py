import sys
sys.stdin = open('omok.txt', 'r')

arr = []
new_arr = [[0 for _ in range(19)] for _ in range(19)]

T = 19
for tc in range(1, T+1):
    arr2 = list(map(int, input().split()))
    arr.append(arr2)

#1. 행 우선순회
for i in range(18):
    for j in range(18):
        cnt_r1 = 0
        cnt_r2 = 0
        for k in range(4):
            num = arr[i][j]
            next = arr[i][j+1]
            if num == 1 and next == 1:
                cnt_r1 += 1
            elif num == 2 and next == 2:
                cnt_r2 += 1
                print(cnt_r2)

        # if cnt_r1 == 4:
        #     print('{}\n{} {}'.format(num, i+1, j))
        # elif cnt_r2 == 4:
        #     print('{}\n{} {}'.format(num, i + 1, j))
#
# #2. 열 우선순회
# for i in range(18):
#     for j in range(18):
#         cnt_c = 0
#         for k in range(4):
#             num2 = arr[j][i]
#             next2 = arr[j][i+1]
#             if num2 == next2 == 1:
#                 cnt_c += 1
#         if cnt_c == 4:
#             print('{}\n{} {}'.format(num2, i+1, j))

# #3. 격자 순회
cnt_rec = 0
for i in range(0, 14):
    for j in range(0, 14):
        for k in range(5):
            for l in range(5):
                pass

