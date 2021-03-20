'''
[1,4,2,3]
[2,1,3,4]


'''
enter = [1,4,2,3]
leave = [2,1,3,4]

len_people = len(enter)
arr = [0]*(len_people+1)

for i in range(1, len_people+1):
    for j in range(1, len_people+1):
        if i!= j:
            if enter.index(i) < enter.index(j) and leave.index(i) > leave.index(j):
                print(i, j)
                arr[i] += 1
            elif enter.index(i) > enter.index(j) and leave.index(i) < leave.index(j):
                print(i, j)
                arr[i] += 1
            elif 0 < enter.index(j) < len_people -1:
                print(i, j)
                for k in range(enter.index(j), len_people):
                    if leave.index(k) < leave.index(i):
                        arr[i] += 1
print(arr[1:])