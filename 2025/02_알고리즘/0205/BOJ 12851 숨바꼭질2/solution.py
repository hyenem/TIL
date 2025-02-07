# 가는 방법을 set으로 받아서,, 계속 문제가 발생,,,
# 방법의 수를 계산할 때에는 같은 칸으로 가더라도 다른 방법으로 가면 다르게 계산해줘야함,,,,,,,,,,,

from collections import deque

N, K = map(int, input().split())

if N>=K:
    print(N-K)
    print(1)
else:
    q = deque()
    q.append((0, K))
    M = max(N+1, 2*K+1)
    visited = [M]*M
    visited[K]=0
    ans = [0, 0]

    while q:
        cnt, item = q.popleft()
        if item == N:
            ans[0]=cnt
            ans[1]+=1
            break
        s = [item+1, item-1]
        if item%2 ==0 and item != 0:
            s.append(item//2)
        for ele in s:
            if 0<=ele<M and visited[ele]>=cnt+1:
                visited[ele]=cnt+1
                q.append((cnt+1, ele))

    while q:
        item = q.popleft()
        if item[0]==ans[0] and item[1]==N:
            ans[1]+=1
    for ele in ans:
        print(ele)