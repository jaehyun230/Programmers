import math

def is_prime(num) :
    for i in range(2, int(math.sqrt(num)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if num % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(n):
    answer = 0
    for i in range (2,n+1) :
        if is_prime(i) :
            answer +=1
    
    return answer
