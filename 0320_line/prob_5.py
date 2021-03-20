program = 'line'
# flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
# commands = ["line -n 100 -s hi -e", "lien -s Bye"]

flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -s 123 -n HI", "line fun"]
answer = []

for i in commands:
    if i.split()[0] != program:  # 일단 프로그램 이름부터 체크, 만약 다르면 뒤 command 더 볼 필요도 없음
        answer.append(False)
        continue
    split_list = i.split()
    flag = False
    #여기까지 왔으면 일단 프로그램 이름은 통과
    type_of_command = ''
    for j in range(1, len(split_list)): #프로그램 이름은 생략하기 위해 1부터 시작
        if split_list[j][0] == '-': #'-'로 시작하면 뒤 문자를 체크
            for k in flag_rules:
                if split_list[j] == k.split()[0]:
                    # print(k.split())
                    type_of_command = k.split()[1]
                    break
        else:
            if type_of_command == 'NULL':
                if j == len(split_list) -1:
                    flag = True
                elif split_list[j+1][0] == '-':
                    flag = True
                else:
                    flag = False
            if ord(split_list[j][0]) >= 65: #ASCII 65 보다 크면 문자
                present_type = 'STRING'
                if present_type == type_of_command:
                    flag = True
            else:   #number
                present_type = 'NUMBER'
                if present_type == type_of_command:
                    flag = True
    answer.append(flag)
print(answer)




