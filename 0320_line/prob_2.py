'''
AaTa+!12-3
aaaaZZZZ)
CaCbCgCdC888834A
UUUUU
ZzZz9Z824

->
[2]
[2, 3, 4]
[1, 4, 5]
[1, 3, 4, 5]
[0]

8 ≤ password 길이 ≤ 15

password는 아래 4 종류의 문자 그룹을 제외한, 다른 어떤 문자도 포함해서는 안됩니다.
[1] 알파벳 대문자(A~Z)
[2] 알파벳 소문자(a~z)
[3] 숫자(0~9)
[4] 특수문자(~!@#$%^&*)

password는 (2.)에서 명시된 4 종류의 문자 그룹 중에서 3 종류 이상을 포함해야 합니다.

password에 같은 문자가 4개 이상 연속될 수 없습니다.

password에 같은 문자가 5개 이상 포함될 수 없습니다.

'''
import re
inp_str = input()
result = []
# rule no. 1
if len(inp_str) > 15 or len(inp_str) < 8:
    result.append(1)
# rule no. 2
rule2_1 = len(re.findall('[A-Z]', inp_str))
rule2_2 = len(re.findall('[a-z]', inp_str))
rule2_3 = len(list(map(int, re.findall('[0-9]', inp_str))))
rule2_4 = len(re.findall('[~!@#$%^&*]', inp_str))
rule_2 = [rule2_1, rule2_2, rule2_3, rule2_4]

# print(inp_str)
# print(rule_2)
if len(inp_str) != sum(rule_2):
    result.append(2)

# rule no. 3
zero_cnt = rule_2.count(0)
if zero_cnt > 1:
    result.append(3)

# rule no. 4
list_str = list(inp_str)
cnt = 0
prev = list_str[0]
for i in range(1, len(list_str)):
    present = list_str[i]
    if present == prev:
        cnt += 1
    else:
        prev = present
    if cnt >= 3:
        result.append(4)
        break
# rule no. 5

for i in list_str:
    if list_str.count(i) > 4:
        result.append(5)
        break

