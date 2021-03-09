'''
BOJ_#1107리모컨
https://www.acmicpc.net/problem/1107

분류가 브루트포스... 반복문을 사용하면서 다 찾아야 하는거 같다
'''

N = int(input())    #이동하려는 채널
M = int(input())    #고장난 버튼 갯수
now = 100   #현위치

if M != 0:
    broken = list(map(int, input().split()))    # 고장난 버튼들
else:
    broken = []
ans = abs(N-now)    #단순 무식하게 +/-로 이동하는 거리


target = N
for i in range(1000000):
    flag = True
    for j in str(i):
        if int(j) in broken:
            flag = False
            break
    #여기 왔다는 것은 숫자로 만들 수 있다는 것
    if flag == True:
        ans = min(ans, len(str(i))+abs(N-i))
print(ans)
