def solution(new_id):
    cnt = 0
    new_id_list = list(new_id)
    operator = ['-', '_', '.']
    new_id_arr = []
    for i in range(len(new_id_list)):
        # 1단계
        new_id_list[i] = new_id_list[i].lower()
    #2단계
    for i in range(len(new_id_list)):
        char = new_id_list[i]
        if 48 <= ord(char) <= 57 or 97 <= ord(char) <= 122 or char in operator:
            new_id_arr.append(char)
    #3단계
    stack = []
    new_id_arr2 = []
    for i in range(len(new_id_arr)):
        if new_id_arr[i] == '.' and len(stack) == 0:
            stack.append(i)
        elif new_id_arr[i] == '.' and len(stack):continue
        elif new_id_arr[i] != '.' and len(stack):
            t = stack.pop()
            new_id_arr2.append('.')
            new_id_arr2.append(new_id_arr[i])
        elif new_id_arr[i] != '.':
            new_id_arr2.append(new_id_arr[i])
    #4단계
    if len(new_id_arr2) > 0:
        if new_id_arr2[0] == '.':
            new_id_arr2 = new_id_arr2[1:]
        elif new_id_arr2[-1] == '.':
            new_id_arr2 = new_id_arr2[0:len(new_id_arr2)]
    #5단계
    if len(new_id_arr2)==0: #빈 문자열이라면
        new_id_arr2 = ['a']
    #6단계
    if len(new_id_arr2) > 15:
        new_id_arr2 = new_id_arr2[0:15]
    if len(new_id_arr2) < 3:
        diff = 3-len(new_id_arr2)
        last = new_id_arr2[-1]
        for _ in range(diff):
            new_id_arr2.append(last)

    if len(new_id_arr2) > 0:
        if new_id_arr2[0] == '.':
            new_id_arr2 = new_id_arr2[1:]
        elif new_id_arr2[-1] == '.':
            new_id_arr2.pop()

    answer = ''
    for k in new_id_arr2:
        answer+=k
    return answer
