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
##전위순회 VLR
def preorder(idx):
    if idx <= last_idx:             #자식 노드가 없을 때 처리
        print(tree[idx], end=' ')
        preorder(2*idx)             #왼쪽자식
        preorder(2*idx+1)           #오른쪽자식
## 중위순회 LVR
def inorder(idx):
    if idx <= last_idx:
        inorder(2*idx)
        print(tree[idx], end=' ')
        inorder(2*idx+1)
## 후위순회 LRV
def postorder(idx):
    if idx <= last_idx:
        postorder(2*idx)
        postorder(2*idx+1)
        print(tree[idx], end=' ')

size = 15
tree = [0]*(size+1)
last_idx = 0        #마지막에 들어온 원소가 위치할 인덱스
for i in range(0, 10):
    #원소넣기
    add(chr(i+65))
#print(tree)

preorder(1)
print()
inorder(1)
print()

postorder(1)
