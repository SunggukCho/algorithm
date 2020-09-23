info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# TC는 모두 통과
# 효율성 실패!

def solution(info, query):
    infos = list(info)
    new_info = []
    for i in infos:
        info = list(map(str, i.split()))
        new_info.append(info)

    querys = list(query)
    new_query = []
    for i in querys:
        query = list(map(str, i.split()))
        while 'and' in query:
            query.remove('and')
        new_query.append(query)

    # for row in new_info:
    #     print(row)
        # for row in new_query:
        #     print(row)
    result = []
    for i in new_query:
        language = i[0]
        job = i[1]
        level = i[2]
        food = i[3]
        score = i[4]
        ans = 0
        #살펴봐야할 목록들
        check_list = []
        check_list.append(int(score))
        if language != '-':
            check_list.append(language)
        if job != '-':
            check_list.append(job)
        if level != '-':
            check_list.append(level)
        if food != '-':
            check_list.append(food)
        for j in new_info:
            cnt = 1
            if check_list[0] <= int(j[4]):
                for k in range(1, len(check_list)):
                    if check_list[k] in j:
                        cnt += 1
                if cnt == len(check_list):
                    ans += 1
        result.append(ans)
    answer = result
    return answer

solution(info, query)
