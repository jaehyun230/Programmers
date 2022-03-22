from collections import deque
#deque를 사용하지않고 pop or remove 등 사용할시 효율성 초과
def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    queue = deque(people)
    while queue :
        if len(queue) >= 2 :
            #가장무거운사람과 가장가벼운사람 비교
            if queue[0] + queue[-1] <= limit :
                queue.pop()
                queue.popleft()
            else :
                queue.popleft()
            answer +=1
        else :
            queue.popleft()
            answer +=1
    
    return answer
