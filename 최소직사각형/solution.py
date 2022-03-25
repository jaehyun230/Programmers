def solution(sizes):
    answer = 0
    max_val = 0
    min_val = 0
    
    for i in sizes :
        if i[0] > i[1] :       
            max_val = max(max_val, i[0])
            min_val = max(min_val, i[1])         
        else :
            max_val = max(max_val, i[1])
            min_val= max(min_val, i[0])
            
    answer = max_val * min_val
    
    return answer
