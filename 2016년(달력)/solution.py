def solution(a, b):
    answer = 0
    #1월1일은 금요일
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    #윤년있는 해
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    
    #해당 달 전날짜 합
    for i in range(a-1):
        answer += months[i]
    
    #해당 달 날짜 추가
    answer += b-1
    answer = answer%7
    
    return days[answer]
