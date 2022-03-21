def solution(phone_number):
    phone_number = list(phone_number)
    for i in range (len(phone_number)) :
        if i < len(phone_number)-4 :
            phone_number[i] = '*'
    answer = ''.join(phone_number)
            
    return answer
