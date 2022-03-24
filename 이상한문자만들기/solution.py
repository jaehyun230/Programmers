def solution(s):
    change_s = s.split(" ")
    answer = ''
    for i in range (len(change_s)) :
        for j in range (len(change_s[i])) :
            if j%2 == 0 :
                answer +=change_s[i][j].upper()
            else :
                answer +=change_s[i][j].lower()
        #마지막 아닐경우만 뒤에 공백 추가        
        if i != len(change_s)-1 :
            answer +=' '
        
    return answer
