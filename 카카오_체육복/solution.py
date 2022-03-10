def solution(n, lost, reserve):
    answer = 0
    remove_list = []    
    
    #중복 부분 찾기
    for i in range (len(lost)) :
        if lost[i] in reserve :
            remove_list.append(lost[i])
    # 중복 부분 제거
    for i in range (len(remove_list)) :
        reserve.remove(remove_list[i])
        lost.remove(remove_list[i])
    
    #lost 한 사람들에게 reserve 해줄 count
    count = 0
    for i in range (len(reserve)) :
        if reserve[i]-1 in lost :
            count +=1
        elif reserve[i]+1 in lost :
            count +=1
    #lost보다 reserve해주는 사람이 많을 수 없음
    if len(lost)-count < 0 :
        answer = n
    else :
        answer = n - (len(lost)-count)
            
    return answer
