def solution(numbers):
    answer = []
    #2개 짝지은 합들 append
    for i in range (len(numbers)) :
        for j in range (i+1, len(numbers)) :
            answer.append(numbers[i]+numbers[j])
    #중복제거
    answer = list(set(answer))
    #오름차순 정렬
    answer.sort()
    return answer
