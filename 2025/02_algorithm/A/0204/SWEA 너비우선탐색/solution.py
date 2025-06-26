# pop을 사용하지 않고 queue를 사용하는 방법

T = int(input())
for tc in range(1, T+1):
    # 큐의 시작하는 포인터
    # pop될 때마다 하나씩 증가
    q = []
    head = 0
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    visited = [False]*(V+1)
    visited[1]=True
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    q.append(1)
    while len(q)!=head:
        item = q[head]
        head += 1
        for ele in sorted(adj[item]):
            if not visited[ele]:
                q.append(ele)
                visited[ele]=True
    print(f'#{tc}', *q)