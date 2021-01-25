'''
풀이
- 감소하는 수의 최대값은 9876543210임.
- 0~9까지의 숫자 중에서 하나의 숫자씩만 골라서 역순으로 배열하면 뒤집으면 딱 하나의 감소하는 수가 나옴
- 원소 개수별로 부분집합을 구하고 역순으로 취한 뒤 arr에 넣음
- N값을 입력받고 이 배열의 크기(len(arr))보다 크면 answer=-1
- N값이 len(arr)보다 작으면 answer = arr[N]
'''

from itertools import combinations

num = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
arr = []
for i in range(10):
    arr.append(i)

for i in range(2, 11):
    tmp = list(combinations(num, i))
    for j in tmp:
        ans = ''
        for k in range(i):
            ans += str(j[i-k-1])
        arr.append(int(ans))

arr.sort()
N = int(input())
if N >= 1023:
    answer = -1
else:
    answer = arr[N]

print(answer)
