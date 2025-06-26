import heapq

N = int(input())
q = []
arr = [int(input()) for _ in range(N)]
for ele in arr:
    if ele==0:
        if q: print(heapq.heappop(q))
        else : print(0)
    else :
        heapq.heappush(q, ele)

