def solution(n):
    answer = 0  
    tmp = ""
    #3진법 변환
    while n > 0 :
        tmp += str(n%3)
        n = n // 3
    # 문자열 거꾸로 뒤집으면 3진법
    #tmp = tmp[::-1]
    answer = (int(tmp,3))
    
    return answer
