T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)

    start, end = map(int, input().split())
    # 시작점을 stack에 넣어둠
    stack = [start]
    visited = [False]*(V+1)
    ans = 0
    while stack:
        # 끝나는 점을 만나면 정답을 1로 만들고 멈추기
        item = stack.pop()
        if item==end:
            ans += 1
            break

        # end가 아닌 경우
        # 이미 들렀던 곳이면 넘어가기
        if visited[item]:
            continue

        # 아니면 방문 표시하고
        visited[item]=True
        # 연결된 점들 중 방문하지 않은 점들 stack에 넣어주기
        for ele in adj[item]:
            if not visited[ele]:
                stack.append(ele)
    print(f'#{tc} {ans}')
