'''
BOJ_#1327소트게임
https://www.acmicpc.net/problem/1327
3 3
3 2 1
-> 1

5 3
5 4 3 2 1
-> 4

'''
from collections import deque
from copy import deepcopy

N, K = map(int, input().split())
arr = list(input().split())
sorted_arr = sorted(arr)    #답 - 정렬된 상태

result = -1
ans = -1
visited = set() # -> 수정1차. set으로 해야 시간 초과 안남
Q = deque()

string = "".join(arr)
visited.add(string)
Q.append(string)

while len(Q):
    ans += 1
    for _ in range(len(Q)):
        cur_str = Q.popleft()
        if cur_str == "".join(sorted_arr): #현재 값이 sorted_arr와 같다면 끝
            result = ans    #ans와 result구분해줘야 함. 안그러면 못찾는 경우에 ans를 출력하면 틀림.
            break
        for i in range(N-K+1):
            new_arr = deepcopy(list(cur_str))
            changing_area = new_arr[i:i+K]  #K길이 만큼 정렬되는 부분
            changing_area.reverse() #sort가 아닌 뒤집기임 -> reverse()

            for j in range(K):
                new_arr[i+j] = changing_area[j]

            new_str = "".join(new_arr)
            if new_str not in visited:  #처음 보는 문자열이라면 Q와 visited에 추가
                visited.add(new_str)
                Q.append(new_str)

print(result)
