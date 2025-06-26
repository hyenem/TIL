# dfs+dp로 leaf 노드 찾아서 아래서부터 갱신해주면서
# 실행 시간을 줄여보려고 했으나
# cycle 이 발생하는 경우 해결 불가

# 완전탐색으로 해결할것,,,

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    if A==B: continue
    # B에서 A로 갈 수 있음
    adj[B].append(A)

maximum = 0
ans = []
for i in range(1, N+1):
    q = [i]
    visited = [False]*(N+1)
    visited[i]=True
    pointer = 0
    while pointer<len(q):
        item = q[pointer]
        pointer+=1
        # 연결되어있는 컴퓨터의 개수마다 카운트 하나씩 올려주기
        for ele in adj[item]:
            if not visited[ele]:
                q.append(ele)
                visited[ele]=True
    # 연결된 개수 최댓값 갱신되면 지금까지 저장되어있는 것 버리기
    if maximum<len(q):
        maximum = len(q)
        ans.clear()
    # 개수가 최대인 경우 답에 넣어주기
    if maximum==len(q):
        ans.append(i)
print(*ans)
