T = int(input())
for tc in range(1, T+1):
    char = list(input())
    stack = []

    for i in range(len(char)):
        if len(stack) == 0:                 #처음에 비웠으면 채우기
            stack.append(char[i])
        elif char[i] != stack[-1]:
            stack.append(char[i])
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                continue

    print('#{} {}'.format(tc, len(stack)))