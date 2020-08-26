import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    M = input()             #포함될 문자
    N = input()             #포함할 문자

    cnt = 0                 #결정 변수
    for i in range(len(N)-len(M)+1): #N에서 M의 길이만큼을 뺀 만큼 순회할 예정, +1을 까먹지 말자.
        if M == N[i:i+len(M)]:       #순회도중 N의 i~i+len(M) 만큼의 길이가 M과 똑같다면, M이 포함되어 있다는 얘기
            cnt += 1                 #그 경우에만 cnt +=1 해주고
        if cnt == 1:break            #cnt가 1이면 더 볼 것도 없이 break
    print('#{} {}'.format(tc, cnt))