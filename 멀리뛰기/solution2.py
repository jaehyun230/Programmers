def solution(n):
    #점프 0 ,1 칸 초기화
    jump = [1, 1]
    
    for i in range (2, n) :
        jump.append((jump[i-1]+jump[i-2]))
    
    return jump[-1]%1234567
