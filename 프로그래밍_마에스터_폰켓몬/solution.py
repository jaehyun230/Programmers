def solution(nums):
    answer = 0
    get = len(nums)//2    
    nums = list(set(nums))
    
    if len(nums) < get :
        return len(nums)
    else :
        return get
    
