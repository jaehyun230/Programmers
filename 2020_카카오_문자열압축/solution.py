def solution(s):
    answer = len(s)
    half = len(s)//2
    
    for i in range (1, half+1) :
        answer_i = len(s)
        #비교 문자열
        temp = s[:i]
        cursor = i
        #반복 카운트
        count = 1
        #중복 숫자 앞에 붙이는 값 길이 
        count_num = 10
        while cursor+i <= len(s) :
            if temp == s[cursor:cursor+i] :
                count+=1
                answer_i -=i
                #첫중복 앞에 숫자붙이는 값 길이
                if count == 2 :
                    answer_i +=1
                # 카운트 자릿수가 증가할때
                if count == count_num :
                    answer_i +=1
                    count_num *=10
                
            else :
                temp = s[cursor:cursor+i]
                count = 1
                count_num = 10
            
            cursor +=i
        
        answer = min(answer, answer_i)
         
    return answer
