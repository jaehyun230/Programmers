def solution(n):
    answer = 0
    n = str(n)
    
    for i in range (len(n)-1, -1, -1) :
        answer  += int(n[i])
        
    return answer
