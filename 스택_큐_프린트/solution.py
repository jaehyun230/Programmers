from collections import deque

def solution(priorities, location):
    
    queue = deque(priorities)
    answer = 0
    while queue :
        length = len(queue)
        prior = queue.popleft()
        for i in range(len(queue)) :
            if prior < queue[i]:
                queue.append(prior)
                # 타겟팅 차례인데 우선순위가 낮을 경우
                if location == 0 :
                    location += len(queue)
                break
        # 인쇄
        if length > len(queue) :
            answer +=1
            # 타겟팅 인쇄할 경우
            if location == 0 :
                return answer
        location -=1
