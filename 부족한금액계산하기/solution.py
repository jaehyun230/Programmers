def solution(price, money, count):
    cost = 0
    for i in range (1, count+1) :
        cost +=i*price

    if money - cost > 0 :
        return 0
    else :
        return abs(money-cost)
    
