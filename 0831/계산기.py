import sys; sys.stdin = open('calc.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(input())

## 1. 후위표기법으로 변경
    #우선순위 설정
    priority = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
        ')': 1,
    }
    stack = []
    output = ''
    for i in arr:
        if i not in '()+-*/':
            output+=i
        elif i == '(':
            #stack에 push
            stack.append(i)
        elif i == ')':
            #'(' 나올때까지 pop
            while stack[-1] != '(':
                if stack[-1] != '(':
                    d1 = stack.pop()
                    output+=d1
            stack.pop()     #'(' 없애기
        #stack이 비어있지 않고, 마지막에 들어있는게 새롭게 추가되는 것보다 우선순위가 낮다면 pop해주고 높은거를 다시 stack에 쌓음
        elif len(stack) != 0 and priority[i] <= priority[stack[-1]]:
            d2 = stack.pop()
            if d2 != '(':
                output += d2
                stack.append(i)
        else:
            stack.append(i)
    while stack:
        d3 = stack.pop()
        if d3 != '(':
            output += d3
## 2. 후위표기법 계산하기
    value_stack = []
    for i in output:
        #연산자가 아닌 숫자들도 str이므로 int로 형변환 해서 stack에 push
        if i not in '()*/+-':
            i = int(i)
            value_stack.append(i)
        elif i == '*':
            val1 = value_stack.pop()
            val2 = value_stack.pop()
            new_val = val1 * val2
            value_stack.append(new_val)
        elif i == '/':
            val1 = value_stack.pop()
            val2 = value_stack.pop()
            new_val = val1 / val2
            value_stack.append(new_val)
        elif i == '+':
            val1 = value_stack.pop()
            val2 = value_stack.pop()
            new_val = val1 + val2
            value_stack.append(new_val)
        elif i == '-':
            val1 = value_stack.pop()
            val2 = value_stack.pop()
            new_val = val1 - val2
            value_stack.append(new_val)
    ans = value_stack[0]
    print('#{} {}'.format(tc, ans))