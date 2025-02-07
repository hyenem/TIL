from collections import deque

N, K = map(int, input().split())

if N>=K:
    print(N-K)
else:
    ans = -1
    q = deque()

    # 도착점 부터 가면 늘 세방향이 아니라 두방향이 되는 경우도 있지 않을까?
    q.append((0,K))
    visited = [False]*(2*K+1)
    visited[K]=True
    flag = False

    while q:
        cnt, item = q.popleft()
        s = {item+1, item-1}
        # 짝수일 때만 나누기 가능
        if item%2==0:
            s.add(item//2)
        for ele in s:
            if ele==N:
                ans = cnt+1
                flag = True
                break
            if 0<=ele<2*K+1 and not visited[ele]:
                visited[ele]=True
                q.append((cnt+1, ele))
        if flag:
            break
    print(ans)