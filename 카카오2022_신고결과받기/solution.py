def solution(id_list, report, k):
    dic = {}
    #중복 제거
    report = list(set(report))
    answer = [0] * len(id_list)
    for a in report :
        x,y = a.split()
        if y not in dic :
            dic[y] = 1
        else :
            dic[y] +=1
    
    for a in report :
        x, y = a.split()
        if dic[y] >= k :
            for i in range (len(id_list)) :
                if id_list[i] == x :
                    answer[i] +=1
    
    return answer
