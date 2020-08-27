def check(char):
    stack = []
    dictionary = {')':'(', '}':'{'}
    for i in char:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i == '}':
            if len(stack) == 0:
                return 0
            else:
                a = stack.pop()
                if dictionary[i] == a:
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
