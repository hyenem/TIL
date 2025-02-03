import heapq

N = int(input())
leftq = []
rightq = []
mid = int(input())
ans = [mid]
for i in range(N-1):
    now = int(input())
    if now<mid:
        if len(leftq)<len(rightq):
            heapq.heappush(leftq, -now)
        else :
            heapq.heappush(rightq, mid)
            heapq.heappush(leftq, -now)
            mid = (-1)*heapq.heappop(leftq)
    else :
        if len(leftq)<len(rightq):
            heapq.heappush(leftq, -mid)
            heapq.heappush(rightq, now)
            mid=heapq.heappop(rightq)
        else :
            heapq.heappush(rightq, now)
    ans.append(mid)
print(*ans)