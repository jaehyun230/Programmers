def solution(s, n):
    answer = ''
    for i in s :
        #ord 아스키 코드값 반환
        if 97 <= ord(i) <= 122 :
            if ord(i) + n <= 122 :
                answer +=chr(ord(i)+n)
            else :
                answer +=chr(ord(i)+n -122 + 96)
            
        elif 65 <= ord(i) <= 90 :
            if ord(i) + n <= 90 :
                answer +=chr(ord(i)+n)
            else :
                answer +=chr(ord(i)+n -90 + 64)
                
        else :
            answer +=i
    
    return answer
