"""
0000000111100000011000000111100110000110000111100111100111111001100111
7개씩 끊어서 2진수를 10진수로 변환
"""
""" #1. 
b = list(map(int, input()))
bit = []
for i in range(len(b)//7):
    bit.append(b[7*i:7*i+7])

for i in range(len(bit)):
    sum = 0
    for j in range(7):
        if bit[i][j] == 1:
            sum += 2**(6-j)
    print(sum)
"""
"""
2. 01D06079861D79F99F (16진수) 숫자를 10진수로 변환
"""
'''
#binary = format(bin(input()), 'b')
hexa = input()
arr = []

#16진수의 각 숫자들을 10진수 형태로 변환
for i in hexa:
    if 65 <= ord(i) < 71:
        num = ord(i)-55
        arr.append(num)
    else:
        arr.append(int(i))
#해당 숫자들을 2진수로 변환하고 자리수를 4개로 만들기 위해 0을 추가
binary = []
for i in arr:
    bit = format(i, 'b')
    if len(bit) == 1:
        bit = '000'+bit
    elif len(bit) == 2:
        bit = '00' + bit
    elif len(bit) == 3:
        bit = '0' + bit
    binary.append(bit)

#모든 2진수 숫자들을 더해서 string 형태로 만든다(7자리로 쪼개기 위해)
string = ''
for s in binary:
    string += s

#7자리씩 쪼갬
new_arr = []
for k in range(0, len(string), 7):
    part = string[k:k+7]
    new_arr.append(part)

#7자리의 2진수들을 10진수로 변환 & 출력
for j in new_arr:
    print(int(j, 2))

'''

# 교수님 풀이
'''
0F97A3
01D06079861D79F99F
'''
s = input()
n = len(s)
# print(s)
output =""  #2진수 표현을 저장

for i in range(n):
    #16진수 -> 10진수
    d = ord(s[i])- ord('0') if '0' <= s[i] <= '9' else ord(s[i]) - ord('A') + 10
    #10진수 -> 2진수 -> output
    for j in range(3,-1,-1):
        output += '1' if d &(1 <<j) else '0'
print(output)
#2진수 -> (7bit씩 끊어서) 10진수
n2 = len(output)//7 #7개씩 묶으면 몇개가 되는지?
remain = len(output)%7 -1   #7개씩 묶고 남은 개수
for i in range(n2):
    digit = 0   #10진수저장
    for j in range(6,-1,-1):
        digit += int(output[i*7 + j]) * (2**(6-j))
    print(digit)
digit = 0
for j in range(remain,-1,-1):
    digit += int(output[n2*7 + j]) * (2**(remain-j))
print(digit)