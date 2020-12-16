"""
10 8
3
0 3
1 4
0 2
"""
"""
문제는 가로,세로로 자른 뒤 생성되는 사각형 중 최대 넓이를 가지는 사각형을 구하는 것.
어차피 모든 가로와 세로는 한 번쯤 만나게 되어있다. 자르고 난 뒤의 가로, 세로의 길이를 구한다면 넓이는 자동으로 구해진다.
"""
R, C = map(int,input().split())     #전체 가로, 세로
N = int(input())
rows = []                           #가로의 길이들을 넣을 LIST
cols = []                           #세로의 길이들을 넣을 LIST

for i in range(N):
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:                 #가로이면
        rows.append(tmp[1])         #가로의 길이만 rows에 추가
    else:
        cols.append(tmp[1])         #세로이면, 세로의 길이만 cols에 추가
#rows, cols 정렬
#input값은 순서대로 들어오지 않음. 순서대로 하지 않아도 어차피 결과는 똑같으므로 길이를 구하기 쉽게 정렬
rows.sort()
cols.sort()

#rows, cols의 마지막에 R,C를 추가
#rows의 가장 큰 값은 결국 세로의 길이 C가 되므로 가장 뒤에 C추가
rows.append(C)
cols.append(R)

#row의 dist를 구함
i=0
temp_row = 0
temp_col = 0
new_row = []
new_col = []
#하나씩 순서대로 비교하면서 이전값과의 차이(길이)를 new_row에 넣어줌
while i < len(rows):
    temp = rows[i]-temp_row
    new_row.append(temp)
    temp_row = rows[i]
    i+=1
#col의 dist를 구함
j = 0
while j < len(cols):
    temp = cols[j]-temp_col
    new_col.append(temp)
    temp_col = cols[j]
    j+=1
#row와 col 각각의 max값을 구한 뒤 곱하면 최대 넓이가 나옴.
max_row = max(new_row)
max_col = max(new_col)
ans = max_row*max_col
print(ans)
