'''
풀이 접근
1. 일단 방향대로 벽까지 모두 민다. -> 0은 그 방향 반대로 집결
2. 그 다음 방향의 역순대로 순회하면서 같은 숫자가 있으면 *2 하고 뒤 숫자를 0으로 바꾼다
3. 이 과정이 모두 끝나고 다시 0을 반대 방향으로 미는 작업을 한 번 더 한다.
'''

def game(arr, dir):
    #상 - 우 - 하 - 좌
    dx = [-1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            

T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    #방향 정하기
    if M == 'up': dir = 0
    elif M == 'right': dir = 1
    elif M == 'down': dir = 2
    else: dir = 3
    
    #함수호출
    print(game(arr,dir))

