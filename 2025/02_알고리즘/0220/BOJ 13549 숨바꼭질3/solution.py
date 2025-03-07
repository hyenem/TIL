import heapq

N, K = map(int, input().split())

q = [(0, N)]
visited = [100001]*200001
while q:
    t, l = heapq.heappop(q)
    if l==K:
        ans = t
        break
    if l<K:
        if visited[2*l]>t:
            visited[2*l]=t
            heapq.heappush(q, (t, 2*l))
    if l<K:
        if visited[l+1]>t+1:
            visited[l + 1] = t + 1
            heapq.heappush(q, (t+1, l+1))
    if l>0:
        if visited[l - 1] > t + 1:
            visited[l - 1] = t + 1
            heapq.heappush(q, (t+1, l-1))

print(ans)
