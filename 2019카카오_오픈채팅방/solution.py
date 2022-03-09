def solution(record):
    answer = []
    uid = []
    command = []
    name_dic = {}
    
    for i in range (len(record)) :
        temp = record[i].split()
        command.append(temp[0])
        uid.append(temp[1])
        try:
            name_dic[temp[1]] = temp[2]
        except :
            continue
        
    for i in range (len(record)) :
        if command[i] == "Enter" :
            answer.append("{0}님이 들어왔습니다.".format(name_dic[uid[i]]))
        elif command[i] == "Leave" :
            answer.append("{0}님이 나갔습니다.".format(name_dic[uid[i]]))
    
    return answer
