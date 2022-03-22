def solution(numbers):
    
    numbers = list(map(str, numbers))
    #key=lambda x : x*3 해당 x 문자열을 3번 반복후 비교 -> 1000이하 4자리수이기에 3번
    numbers.sort(key=lambda x : x*3, reverse=True)
    answer = "".join(numbers)
    # 0000 과같은 입력문제 해결
    answer = int(answer)
    answer = str(answer)
    return answer
