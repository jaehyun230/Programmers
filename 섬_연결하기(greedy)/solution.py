def solution(n, costs):
    answer = 0
    #연결되지 않은 섬 초기화
    graph = [0] * n
    
    #저렴순으로 정렬
    costs.sort(key = lambda x : x[2])
    
    #시작부분
    graph[costs[0][0]] = 1
    
    #연결되지 않은 섬 있으면 while 문
    while 0 in graph :
        #저렴한 연결부터 체크
        for i in costs :
            if graph[i[0]] == 1 :
                if graph[i[1]] == 0 :
                    graph[i[1]] = 1
                    answer +=i[2]
                    break
            if graph[i[1]] == 1 :
                if graph[i[0]] == 0 :
                    graph[i[0]] = 1
                    answer +=i[2]
                    break
        
    return answer
