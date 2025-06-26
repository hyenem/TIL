from collections import deque

N, K = map(int, input().split())
time = K
anscnt = 0
if N>=K:
    print(N-K)
    print(1)
else :
    visited = [False]*(2*K+1)
    q = deque()
    q.append((0,N))
    while q:
        cnt, item = q.popleft()
        visited[item]=True
        if cnt==time and item==K:
            anscnt+=1
        elif cnt>time:
            break
        for ele in [item+1, item-1, item*2]:
            if 0<=ele<2*K+1 and not visited[ele]:
                if ele==K:
                    time=min(time, cnt+1)
                q.append((cnt+1,ele))
    print(time)
    print(anscnt)