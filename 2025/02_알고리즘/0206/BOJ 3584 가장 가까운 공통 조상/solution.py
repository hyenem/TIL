T = int(input())
for _ in range(T):
    N = int(input())

    # 자식 노드의 인덱스에 부모 노드의 인덱스를 저장
    parent = [0]*(N+1)
    for _ in range(N-1):
        p, c = map(int, input().split())
        parent[c]=p

    v1, v2 = map(int, input().split())
    p1 = [v1]
    p2 = [v2]

    # 주어진 두 노드에서부터 루트로 가는 길 찾기
    while p1[-1]!=0:
        p1.append(parent[p1[-1]])
    while p2[-1]!=0:
        p2.append(parent[p2[-1]])
    ans = -1

    # 공통 부모 노드들 중 가장 아래 찾기
    while p1 and p2 and p1[-1]==p2[-1]:
        p1.pop()
        ans = p2.pop()

    print(ans)