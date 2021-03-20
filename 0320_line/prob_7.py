program = 'line'
flag_rules = ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
commands = ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]

# program = 'bank'
# flag_rules = ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"]
# commands = ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]

answer = []

for i in commands:
    if i.split()[0] != program:  # 일단 프로그램 이름부터 체크, 만약 다르면 뒤 command 더 볼 필요도 없음
        answer.append(False)
        continue
    split_list = i.split()
    #여기까지 왔으면 일단 프로그램 이름은 통과
    type_of_command = ''
    flag = True
    for j in range(1, len(split_list)): #프로그램 이름은 생략하기 위해 1부터 시작
        # print(split_list, split_list[j])
        if split_list[j][0] == '-': #'-'로 시작하면 뒤 문자를 체크, ALIAS를 추가해야함
            for k in flag_rules:
                if 'ALIAS' in k:
                    alias_target = k.split()[2]
                    for t in flag_rules:
                        if alias_target == t.split()[0]:
                            type_of_command = t.split()[1]
                else:
                    if split_list[j] == k.split()[0]:
                        type_of_command = k.split()[1]
                        break
        else:
            print(split_list[j], 'Type', type_of_command)
            if type_of_command == 'NULL':
                if j == len(split_list) -1: #이게 마지막 문자이거나
                    flag = True
                    break
                elif split_list[j+1][0] == '-': #다음 문자로 올 것이 '-'여야한다
                    flag = True
                    break
                else:                       #그렇지 않으면 False!
                    flag = False
                    break
            #-e가 아닌 것들 중 처리하는 PART
            idx = j
            while j <= idx < len(split_list):   #다음 '-' 명령어 등장하기 전까지 반복
                if split_list[idx][0] != '-':   #'-'명령어가 아니면,
                    if ord(split_list[idx][0]) >= 65:   #문자
                        if type_of_command == 'STRINGS':    #문자열이면 계속 True
                            flag = True
                        elif type_of_command == 'STRING':   #단일 문자인데 idx와 j가 다르면 문자열이므로 False
                            flag = True
                            if j != idx:
                                flag = False
                        else:
                            flag = False
                            break
                    elif ord(split_list[idx][0]) < 65:  #숫자
                        if type_of_command == 'NUMBERS' or 'days':
                            if idx-j >= 1:  #반드시 복수여야 함.
                                flag = True
                            else:
                                flag = False
                        elif type_of_command == 'NUMBER':
                            if j != idx:
                                flag = False
                        else:
                            flag = False
                            break
                else:
                    break
                idx += 1
            print('flag', flag)
    #     if not flag:
    #         answer.append(False)
    #         break
    # if flag:
    #     answer.append(True)


print(answer)




