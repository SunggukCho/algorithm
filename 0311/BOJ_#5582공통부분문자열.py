'''
BOJ_#5582공통부분문자열 -> 시간초과
https://www.acmicpc.net/problem/5582
흠... 누가봐도 이렇게 안푸는게 맞는 것 같긴한데, 맞는 방법이 안떠오르네..


ABRACADABRA
ECADADABRBCRDARA
'''
string_A = list(input())
string_B = list(input())

result = 0
for i in range(len(string_A)):
    start = string_A[i]
    maxV = 0
    for j in range(len(string_B)):
        tmp = []
        if string_B[j] == start:
            idx = 0
            for k in range(1, len(string_B) - j):
                if string_A[i:i+k] == string_B[j:j+k]:
                    idx += 1
            tmp.append(idx)
        if len(tmp) != 0:
            if max(tmp) > maxV:
                maxV = max(tmp)
    if result < maxV:
        result = maxV
print(result)
