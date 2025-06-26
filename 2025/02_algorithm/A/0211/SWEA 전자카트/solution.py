# 우선순위큐
import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    q = []
    heapq.heappush(q, (0, -1, 0, 1))
    while q:
        p, cnt, x, visited = heapq.heappop(q)
        if cnt==(-1)*N:
            heapq.heappush(q, (p+arr[x][0], cnt-1, 0, visited))
            continue
        elif cnt==(-1)*N-1:
            ans = p
            break
        for i in range(N):
            if (visited>>i)&1==1: continue
            heapq.heappush(q, (p+arr[x][i], cnt-1, i, visited|(1<<i)))

    print(f'#{tc} {ans}')