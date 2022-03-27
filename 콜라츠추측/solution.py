def solution(num):
    count = 0
    #시작부터 1일경우
    if num == 1 :
        return 0
    while count < 500 :
        #짝수의 경우
        if num % 2 == 0 :
            num = num//2
            count +=1
        #홀수의 경우
        else : 
            num = (num*3)+1
            count +=1
        
        if num == 1 :
            return count
        
    return -1
