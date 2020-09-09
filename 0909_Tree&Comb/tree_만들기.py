def isFull():
    return last_idx == size
def isEmpty():
    return last_idx == 0
def add(n):  #원소추가
    global last_idx
    last_idx += 1
    if isFull():
        print("Tree is full")
        return
    tree[last_idx] = n

size = 15
tree = [0]*(size+1)
last_idx = 0        #마지막에 들어온 원소가 위치할 인덱스
for i in range(0, 15):
    #원소넣기
    add(chr(i+65))
print(tree)
