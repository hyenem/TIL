T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    stack = [1]
    ans = []
    visited = [False]*(V+1)
    # 처리해야할 엣지가 남지 않을 때 까지
    while stack:
        # 가장 마지막에 들어간(먼저 처리해야할) 원소를 처리
        item = stack.pop()
        # 이미 방문한 곳이면 넘어가기
        if visited[item]:
            continue
        # 방문하지 않았으면 정답에 넣어주고 방문표시
        visited[item]=True
        ans.append(item)
        # 이번에 방문한 노드에 연결된 노드들 중
        # 아직 방문하지 않은 노드를 다음 방문한 노드에 넣어주기
        # 단, 낮은 순서부터 방문해야하므로 큰 숫자부터 넣어주기
        for ele in sorted(adj[item], reverse=True):
            if not visited[ele]:
                stack.append(ele)

    print('#'+str(tc), *ans)