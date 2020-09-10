import sys;
sys.stdin = open('sample_input.txt', 'r')
def make_tree(n):
    global cnt
    if n <= N:
        #왼쪽 idx는 n*2
        make_tree(n*2)
        tree[n] = cnt
        cnt+=1
        #오른쪽 idx는 n*2+1
        make_tree(n*2+1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [i for i in range(1, N + 1)]
    tree = [0] * (N+1)

    cnt = 1
    top = N//2+1

    make_tree(1)

    top = tree[1]
    dist = N//2
    ans = tree[dist]

    print('#{} {} {}'.format(tc, top, ans))
