from collections import deque

T = int(input())
for tc in range(1, T+1):
    ans = 0
    N, M = map(int, input().split())
    arr = [0]+list(map(int, input().split()))
    q = deque()
    q.append((1, 0, 0))
    while q:
        size, location, time = q.popleft()
        ans = max(size, ans)
        if time+1<=M:
            if location+1<N+1:
                q.append((size+arr[location+1], location+1, time+1))
            if location+2<N+1:
                q.append((size//2+arr[location+2], location+2, time+1))
    print(f'#{tc} {ans}')

