'''
(@&
?/--
/(\
?
#

158
1984
-47
4

'''


num = {
    '-': 0,
    '\\': 1,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
    '/': -1,
}
while True:
    N = list(input())
    num_len = len(N)
    ans = 0
    if N[0] == '#':
        break

    for i in range(num_len):
        ans += num[N[i]]*8**(num_len-i-1)
    print(ans)