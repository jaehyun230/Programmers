def solution(s):
    count1 = 0
    count2 = 0
    for i in s :
        if i == 'p' or i == 'P' :
            count1 +=1
        if i == 'y' or i == 'Y' :
            count2 +=1

    if count1 == count2 :
        return True
    
    return False
