'''
BOJ_#문자열폭발
https://www.acmicpc.net/problem/9935
문제의 핵심은 bomb의 첫글자로 판단하는게 아니라 마지막 글자로 폭발문자열인지 체크하는 것이었음

'''
text = list(input())    #텍스트
bomb = input()    #폭발문자열 배열
len_bomb = len(bomb)

stack = []

for i in text:
    stack.append(i)
    if i == bomb[-1] and ''.join(stack[-len_bomb:]) == bomb:
        del stack[-len_bomb:]

answer = ''.join(stack)
if len(answer) == 0:
    print('FRULA')
else:
    print(answer)
