import sys; sys.stdin = open('inorder.txt','r')

## 중위순회 LVR
def inorder(idx):
    global result
    if idx <= last_idx:
        inorder(2*idx)
        result += inorder_list[idx]
        inorder(2*idx+1)
    return result
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        k = list(input().split())
        arr.append(k)

    inorder_list = [0]*(N+1)
    new_arr = []
    for i in arr:
        if len(i) == 4:
            node = int(i[0])
            char = i[1]
            left = int(i[2])
            right = int(i[3])
            new_arr.append([node, char, left, right])
        elif len(i) == 3:
            node = int(i[0])
            char = i[1]
            left = int(i[2])
            new_arr.append([node, char, left])
        else:
            node = int(i[0])
            char = i[1]
            new_arr.append([node, char])

    #루트값 inorder_list에 넣어주기
    for i in new_arr:
        inorder_list[i[0]] = i[1]

    last_idx = len(inorder_list) -1
    result=''
    ans = inorder(1)
    print('#{} {}'.format(tc,ans))