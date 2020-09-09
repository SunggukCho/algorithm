data = [-7, -3, -2, 5, 8]
N = len(data)

sum_list = []
for i in range(1 << N):
    new_list = []
    for j in range(N):
        if i & (1 << j):
            new_list.append(data[j])
    sum_list.append(new_list)

for i in sum_list:
    if sum(i) == 0:
        print(True, i)
# 강사님 풀이
data = [-7, -3, -2, 5, 8]
N = len(data)
ans = False
for i in range(1<<N):
    sum = 0
    for j in range(N):
        if i & (1<<j):


    if 