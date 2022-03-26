def solution(N, stages):
    stage_div = len(stages)    
    lose_list = []
    answer = []
    
    for i in range(1, N+1) :
        count = 0
        
        for j in range(len(stages)) :
            if i == stages[j] :
                count +=1
        if count == 0 :
            lose_list.append(0)
        else :
            lose_list.append(count/stage_div)
            stage_div -=count
            
    lose_sort = sorted(lose_list, reverse=True)
    
    for i in lose_sort :
        for j in range (len(lose_list)) :
            if i == lose_list[j] :
                lose_list[j] = -1
                answer.append(j+1)
                
    return answer
