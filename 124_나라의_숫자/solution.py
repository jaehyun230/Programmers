def my_base_conversion(n, q):
    rev_base = ''
    while n > 0:
        # 시작 할때 값 1 카운트를 맞추기 위해서 -1
        n, mod = divmod(n-1, q)
        rev_base += str(mod)
    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

def solution(n):
    answer = my_base_conversion(n, 3)
    answer = answer.replace('2','4')
    answer = answer.replace('1','2')
    answer = answer.replace('0','1')
    
    return answer
