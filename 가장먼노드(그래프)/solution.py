from collections import deque

def solution(n, edge):
    answer = 0
    #그래프 초기화
    graph = [[] for i in range (n+1)]
    #1번 노드부터 거리 초기화
    route = [0]*(n+1)
    
    #그래프 edge 추가
    for i in range (len(edge)) :
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
    
    queue = deque()
    #node 1번부터 시작
    queue.append(1)
    move = 0
    while queue :  
        start = queue.popleft()
        for i in graph[start] :
            if route[i] == 0 :
                route[i] = route[start]+1
                queue.append(i)
    #시작노드는 거리 0            
    route[1] = 0    
    max_route= max(route)
    for i in route:
        if i == max_route:
            answer+=1     
    
    return answer
