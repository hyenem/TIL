from collections import deque

def combination(idx, dist):
    global ans
    # 정답보다 차가 작아졌을 때
    if abs(dist)<ans:
        # 빨간 구역끼리 다 연결되어있나?
        visited = [0]*(N+1)
        q = deque([1])
        visited[1]=1
        while q:
            x = q.popleft()
            for nx in adj[x]:
                if visited[nx]: continue
                if nx not in red: continue
                visited[nx]=1
                q.append(nx)
        if sum(visited)==len(red):
            # 빨간 구역 다 연결했으면
            # 나머지 구역은 다 연결되어있나?
            for k in range(2, N+1):
                if visited[k]: continue
                q = deque([k])
                visited[k]=1
                while q:
                    x = q.popleft()
                    for nx in adj[x]:
                        if visited[nx]: continue
                        visited[nx]=1
                        q.append(nx)
                break
            # 그렇다면 정답 갱신
            if sum(visited)==N:
                ans = abs(dist)

    # 모두다 빨간구역이면 안되니까
    if len(red)==N-1:
        return

    # 빨간구역에 추가하기(조합)
    for i in range(idx+1, N+1):
        red.append(i)
        combination(i, dist-2*popular[i])
        red.pop()

N = int(input())
popular = [0]+list(map(int,input().split()))
adj = [0]
for _ in range(N):
    K, *lst = map(int,input().split())
    adj.append(lst)

all = sum(popular)
ans = 2*all
# 빨간구역 일단 1은 넣고 시작(구획이니까 어느 구역인지는 안중요)
red = [1]
combination(1, all-2*popular[1])

if ans==2*all:
    print(-1)
else: print(ans)