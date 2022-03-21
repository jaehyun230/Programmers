from collections import deque

#연결된 네트워크 모두 방문처리
def bfs(num, n, computers) :
    queue = deque()
    queue.append(num)
    
    while queue :
        which = queue.popleft()
        for i in range (n) :
            if computers[which][i] == 1 :
                computers[which][i] = 0
                queue.append(i)

def solution(n, computers):
    answer = 0
    #네트워크 컴퓨터 수만큼
    for i in range (n) :
        #해당 컴퓨터 네트워크가 연결체크 안했을경우
        if computers[i][i] == 1 :
            bfs(i, n, computers)
            answer +=1
                
    return answer
