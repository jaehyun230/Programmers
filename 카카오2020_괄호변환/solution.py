#u,v 로 문자열 분리
def divide_array(array) :
    left = 0
    right = 0
    for i in range(len(array)): 
        if array[i] == '(' :
            left +=1
        else :
            right +=1
        if left == right :
            u = array[:i+1]
            v = array[i+1:]
            break
    return u, v

#올바른 괄호 문자열 확인
def is_correct(array) :
    stack = []
    for i in array :
        if i == '(' :
            stack.append(i)
        else :
            if len(stack) == 0 :
                return False
            else :
                stack.pop()
    return True

#올바른 괄호 문자열로 변환 작업
def change_correct(p):
    result = ""
    if not len(p): return ""
    u,v = divide_array(p)
    if is_correct(u):
        result = u + change_correct(v)
    else:
        tmp = "("
        tmp += change_correct(v)
        tmp += ")"
        u = u[1:-1]
        for c in u:
            if c == '(':
                tmp+=')'
            else:
                tmp+='('
        result += tmp
    return result

def solution(p):
    #처음 부터 올바른 괄호  문자열 일경우
    if is_correct(p) :
        return p
    
    answer = change_correct(p) 
    
    return answer
