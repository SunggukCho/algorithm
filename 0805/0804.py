# 0. while 과 익숙해지기
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73: break
    print(i, end=" ")
    i+=1

"""
N과 다음 줄에 N개의 양의 정수 Ai가 주어진다. 0 <= i < N
8
7 2 4 3 6 2 4 5
"""
# 1. 짝수인 정수의 개수는?
T = int(input())
count = []
numbers = list(map(int, input().split()))
for i in range(1, T+1):
    if numbers[i] % 2 == 0:
        count.append(numbers[i])
result = len(count)
print(result)

# 2. A1 ~ AN-1에 대해 바로 왼쪽의 숫자보다 큰 숫자의 개수는?
T = int(input())
count = []
numbers = list(map(int, input().split()))
for i in range(2, T+1):
    if numbers[i] > numbers[i-1]
        count.append(numbers[i])
result = len(count)
print(result)

# 3. Ai에 대해 왼쪽에서 가장 작은 수와의 차이([Ai - minV])를 출력하는 프로그램을 만드시오. (1 < i < N-1)
T = int(input())
count = []
left = []
numbers = list(map(int, input().split()))
for i in range(1, T+1):
    for j in range(1, i):
        left.append(numbers[j])
    result = numbers[i] - min(left)
    print(result)

# 4. Ai에 대해 오른쪽에서 가장 큰 수와의 차이를 출력하는 프로그램을 만드시오. (0 < i < N-2)


# 5. N개의 정수에서 연속으로 증가하는 숫자의 개수를 증가구간의 길이라고 한다. 가장 긴 증가구간의 길이를 출력하는 프로그램을 만드시오.
# 최소 증가구간의 길이는 1이다.



# 6. N과 M이 주어진다. N개의 정수가 입력될 때 M보다 큰 수의 개수를 출력하시오.
"""
8 5
7 2 4 3 6 2 4 5 
"""

# 7.










