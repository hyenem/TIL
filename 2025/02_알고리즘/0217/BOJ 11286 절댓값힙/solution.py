import heapq

N = int(input())
q = []
arr = [int(input()) for _ in range(N)]
for ele in arr:
    if ele==0:
        if q:
            num, pm = heapq.heappop(q)
            print(num*pm)
        else : print(0)
    else :
        heapq.heappush(q, (abs(ele), -1 if ele<0 else 1))