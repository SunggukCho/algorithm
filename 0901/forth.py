import sys; sys.stdin = open('forth.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())

    operator = ['*', '/', '+', '-']
    num_digit = 0
    num_operator = 0

    output = []
    result = 0
    for i in range(len(arr)-1):
        if arr[i] not in operator:
            arr[i] = int(arr[i])
            num_digit += 1
            output.append(arr[i])
        elif arr[i] == '*':
            num_operator += 1
            if len(output) != 0:
                val1 = output.pop()
            if len(output) != 0:
                val2 = output.pop()
                new_val = val2 * val1
                output.append(new_val)
            else:
                result = 'error'
        elif arr[i] == '/':
            num_operator += 1
            if len(output) != 0:
                val1 = output.pop()
            if len(output) != 0:
                val2 = output.pop()
                new_val = val2 // val1      #이거 /로 하면 ㅈ된다...
                output.append(new_val)
            else:
                result = 'error'
        elif arr[i] == '+':
            num_operator += 1
            if len(output) != 0:
                val1 = output.pop()
            if len(output) != 0:
                val2 = output.pop()
                new_val = val1 + val2
                output.append(new_val)
            else:
                result = 'error'
        elif arr[i] == '-':
            num_operator += 1
            if len(output) != 0:
                val1 = output.pop()
            if len(output) != 0:
                val2 = output.pop()
                new_val = val2 - val1
                output.append(new_val)
            else:
                result = 'error'

    if len(output) != 0 and num_digit-1 == num_operator:
        result = output[0]
    else:
        result = 'error'

    print('#{} {}'.format(tc, result))
