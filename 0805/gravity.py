def gravity(data):
    top = 0    #리스트 꼭대기 값
    idx = 0    #과거 최대값의 index
    cnt = 0
    new_list = []
    for i in data:
        len_top = len(i)
        if len_top >= top:
            top = len_top
            diff = data.index(i) - idx
            new_list.append(diff)
            idx = data.index(i)
        else:
            diff = data.index(i) - idx
            new_list.append(diff)
            if data.index(i)+1 == len(data):
                diff = len(data)-idx
                new_list.append(diff)
        print(new_list)
    return max(new_list)

data = [[1,2,3,4,5,6,7],[1,2,3,4,],[1,2],[],[1],[1,2,3,4,5,6],[1],[1,2,3,4,5,6,7]]
result = gravity(data)
print(result)


""" 
 풀이법
1. 왼쪽에 있는 (리스트의 초반부에 나오는 것)리스트의 가장 큰 값을 찾는다
2. for 문을 돌려서 이전값보다 len가 더 큰 리스트가 있으면 break하고 길이의 차이를 구한다
3. 그 다음 리스트의 꼭대기가 자기 보다 크지 않다면 continue
4. 이 낙차들을 새로운 리스트에 append하고, 이 중에서 max값을 return
"""