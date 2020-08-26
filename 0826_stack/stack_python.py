stack = []
def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        print("Stack is empty")
        return
    else:
        return stack.pop()

push(1)
push(2)
push(3)

print(stack)

print(pop())
print(pop())
print(pop())

print(stack)