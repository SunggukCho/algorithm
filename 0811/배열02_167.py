arr = [[16, 27], [39, 100], [19, 88], [61, 20]]

#가로평균
for i in range(len(arr)):
    temp_row = []
    temp_column = []
    for j in range(len(arr[i])):
        temp_row.append(arr[i][j])
    print(sum(temp_row)//2, end = ' ')
print() #빈줄

#세로평균
for i in range(len(arr[j])):
    temp_column = []
    for j in range(4):
        temp_column.append(arr[j][i])
    print(sum(temp_column)//4, end = ' ')
print() #빈줄

#총평균
result = 0
for i in range(len(arr)):
    rows = 0
    for j in range(len(arr[j])):
        rows += arr[i][j]
    result += rows
    
print(result//8)
