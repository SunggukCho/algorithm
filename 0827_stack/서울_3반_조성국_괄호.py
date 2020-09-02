def check(char):
    stack = []
    dictionary = {')':'(', '}':'{'}
    for i in char:
        if i == '(' or i == '{':        #여는 괄호 stack append
            stack.append(i)
        elif i == ')' or i == '}':      #닫는 괄호 stack pop
            if len(stack) == 0:         #pop 할때는 stack 길이 0인지 체크
                return 0
            else:
                a = stack.pop()
                if dictionary[i] == a:  #괄호 종류에 따라 순서 다를 수 있으므로 체크
                    continue
                else:
                    return 0
    if len(stack) == 0:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    char = list(input())
    print('#{} {}'.format(tc, check(char)))
