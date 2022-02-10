def solution(strings, n):
    answer = []
    
    for i in range (len(strings)) :
        strings[i] = strings[i][n] + strings[i] # 앞에 구분 정렬 구분값추가
    strings.sort()
    for j in range(len(strings)):
        answer.append(strings[j][1:])
    
        
    return answer
