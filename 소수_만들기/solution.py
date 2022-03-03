import math
from itertools import combinations

# 소수 판별
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
                    
def solution(nums):
    answer = 0
    nums = list(combinations(nums,3))
    for i in range(len(nums)) :
        is_prime = is_prime_number(nums[i][0]+nums[i][1]+nums[i][2])
        if is_prime == True :
            answer +=1

    return answer
