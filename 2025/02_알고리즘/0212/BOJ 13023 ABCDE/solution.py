def solution(idx, cnt):
    if cnt==4: return True
    # 인접행렬 중 방문하지 않은 곳
    for ele in adj[idx]:
        if visited[ele]: continue
        visited[ele]=True
        flag = solution(ele, cnt+1)
        if flag: return True
        visited[ele]=False
    return False



N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

visited = [False]*N
# 모든 사람을 시작으로 채크함
for i in range(N):
    visited[i]=True
    ans = solution(i, 0)
    if ans: break
    visited[i]=False

if ans:
    print(1)
else:
    print(0)