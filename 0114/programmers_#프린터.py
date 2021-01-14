def solution(priorities, location):
    arr = [i for i in range(len(priorities))]
    answer = ans = 0
    while len(priorities):
        start = priorities.pop(0)
        arr_start = arr.pop(0)
        for i in priorities:
            if i > start:
                priorities.append(start)
                start = 0
                arr.append(arr_start)
                break
            else:
                continue
        if start != 0:
            ans += 1
        if arr_start == location:
            answer = ans
    return answer


# priorities = [2, 1, 3, 2]
# location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0
num = solution(priorities, location)
print(num)