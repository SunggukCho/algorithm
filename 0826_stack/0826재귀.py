# def summation(n):
#     if n == 1:
#         return 1
#     else:
#         return n+summation(n-1)
#
# print(summation(10))

def bracket(item):
    for i in range(len(item)):
        if item[i] == '{':
            stack.append(i)
        elif item[i] == '}':
            if len(stack) == 0:
                return print('Stack is empty')
            break
            else:
                return stack.pop()

stack = []
char = '{}{{{}}}}'

print(bracket(char), stack)