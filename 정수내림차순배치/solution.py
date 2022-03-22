def solution(n): 
    #int(n)을 입력값이 정수가 아닐수 있음으로 추가로 해줘야함
    numbers = list(str(int(n)))
    numbers.sort(reverse = True)
    return int("".join(numbers))
