import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville :
        heapq.heappush(heap, i)
    
    while len(heap) >= 2 :
        #제일 맵지않은 지수
        scov = heapq.heappop(heap)
        
        if scov >= K :
            break
        
        if scov < K :
            #두번째로 맵지않은 스코빌 지수
            scov2 = heapq.heappop(heap)
            heapq.heappush(heap, scov+(scov2*2))
            answer +=1
            
    #섞은 활동후 가장 낮은 스코빌 지수 음식
    min_scov = heapq.heappop(heap)
    if min_scov < K :
        return -1
    
    return answer
