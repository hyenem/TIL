import heapq

N, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

bags = [int(input()) for _ in range(K)]
bags.sort()

ans = 0
idx = 0
q = []
for bag in bags:
    while idx<N and arr[idx][0]<=bag:
        heapq.heappush(q, -arr[idx][1])
        idx += 1
    if q:
        ans += -heapq.heappop(q)

print(ans)