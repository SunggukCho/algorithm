def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(':            #왼쪽 괄호면 push
          stack.append(arr[i])
        elif arr[i] == ')':          #오른쪽 괄호면 pop
            if len(stack) == 0:
                print('Stack is empty')
                return False
            else:
                stack.pop()
    if stack: return False
    else: return True

stack = []
arr = '()()((()))'

print(check(arr))
