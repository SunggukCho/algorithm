# front, rear 이용
size = 4
Q = [0]*size
front, rear = 0, 0 # 선형 큐는 -1, -1

def enQueue(item):
    global rear
    if (rear+1) % size == front:      #큐 포화 상태
        print("Queue full")
    else:
        rear = (rear + 1) % size               #
        Q[rear] = item

def deQueue():
    global front
    if front == rear:                #큐 empty 비어있는 상태
        print('Queue is empty')
    else:
        front += 1
        return Q[front]

def Qpeek():
    if front == rear:
        print("Queue Empty")
    else:
        return Q[(front +1) % size]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(Q)