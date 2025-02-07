# 이렇게 풀면 cycle이 등장했을 때 해결 불가

def dfs(s):
    for ele in adj[s]:
        # 아직 다음 노드가 계산 전이면
        # 다음 노드에 연결된 개수 계산
        if not visited[ele]:
            visited[ele]=True
            dfs(ele)
        # 이전 노드에 다음노드에 연결된 개수 더해주기
        cnt[s]+=cnt[ele]

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    if A==B: continue
    # B에서 A로 갈 수 있음
    adj[B].append(A)

cnt = [1]*(N+1)
visited=[False]*(N+1)
maximum = 0
for i in range(1, N+1):
    if visited[i]:
        continue
    visited[i]=True
    dfs(i)
    maximum = max(maximum, cnt[i])

ans = []
for i in range(1, N+1):
    if cnt[i]==maximum:
        ans.append(i)

print(*ans)