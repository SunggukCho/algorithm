'''
BOJ_#2252줄세우기
https://www.acmicpc.net/problem/2252
4 2
4 2
3 1

답: 4 2 3 1

풀이
문제를 읽고서 오랜만에 트리 아니면 힙이라는 느낌을 받았으나 잘 모르겠음...
그냥 맘편하게 배열로 가자
앞에 나온애들이 더 작은거고, 작은 친구들부터 큰친구들 순서대로 출력한다.
'''

N, M = map(int, input().split())
students = [0 for _ in range(N)]  #학생수만큼 0 집어넣기
heights = [[] for _ in range(N)]    #빈 리스트 만들어두고, A보다 뒤에 나오면 집어 넣음
for i in range(M):
    A, B = map(int, input().split())
    students[B-1] += 1
    heights[A-1].append(B-1)

Q = []
for i in range(N):
    if students[i] == 0: #n까지의 수 중에서 가장 작은 축에 속하는 친구들
        Q.append(i)
ans = []
while len(Q):
    k = Q.pop(0)
    ans.append(k+1)
    for j in heights[k]:
        students[j] -= 1    #여러번 나온 친구는 더 큰 친구가 없을 때 까지 줄이기
        if students[j] == 0:    #더 이상 없으면
            Q.append(j)
for row in ans:
    print(row, end=' ')
