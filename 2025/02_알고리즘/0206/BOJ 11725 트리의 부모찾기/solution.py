N = int(input())
adj=[[] for _ in range(N+1)]
parent = [0]*(N+1)
parent[1]=1
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

q=[1]
while q:
    item = q.pop(0)
    for ele in adj[item]:
        # 루트부터 시작하니까
        # 인접노드 중 부모노드가 없으면
        # 내가 부모노드임
        if parent[ele]==0:
            parent[ele]=item
            q.append(ele)

for i in range(2, N+1):
    print(parent[i])