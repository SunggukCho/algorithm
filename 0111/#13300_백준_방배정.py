"""
방 배정 시 올림이 주요 포인트이다.
만약 한 학년의 같은 성별에 K보다 많은 학생(num)이 있다면 방을 num // K + 1 만큼 만들어야 한다.
하지만 이때 num이 K로 딱 나눠 떨어지게 되면 (num % K == 0) +1을 안해줘야 한다.
코드를 좀 더 단순화 하기 위해 math 를 import 하여 ceil(올림)기능을 활용하면 편하다.
"""
import math

N, K = map(int, input().split())

students = [[0] * 7 for _ in range(2)]

for i in range(N):
    S, Y = map(int, input().split())
    students[S][Y] += 1

rooms = 0
for i in students:
    for j in i[1:]:
        rooms += math.ceil(j / K)
print(rooms)
