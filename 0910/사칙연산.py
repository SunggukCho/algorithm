import sys; sys.stdin = open('calc.txt','r')

def postorder(idx):
    global output
    if idx <= last_idx:
        postorder(2*idx)
        output.append(tree[idx])
        postorder(2*idx+1)

T = 1
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    operator = ['*','/','+','-']
    for i in range(N):
        node = list(input().split())
        if node[1] not in operator:
            tree[int(node[0])] = int(node[1])
        else:
            tree[int(node[0])] = node[1]

    #print(tree)
    last_idx = N
    output = []
    postorder(1)
    print(output)

