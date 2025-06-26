from collections import deque

# 멘허튼 거리 계산해주는 함수
def distance(s, e):
    return abs(s[0]-e[0])+abs(s[1]-e[1])

T = int(input())
for _ in range(T):
    N = int(input())
    house = tuple(map(int, input().split()))
    store = [tuple(map(int, input().split())) for _ in range(N)]
    # 인덱스가 i번쨰인 편의점에 방문표시
    visited = [False]*N
    festival = tuple(map(int, input().split()))

    q = deque()
    q.append(house)
    ans = 'sad'
    while q:
        # 페스티벌까지 갈 수 있으면 가기
        item = q.popleft()
        if distance(item, festival)<=1000:
            ans = 'happy'
            break
        # 행복한채로 갈수 있는 편의점 다 보기
        for i in range(N):
            if visited[i]:
                continue
            if distance(item, store[i])<=1000:
                visited[i]=True
                q.append(store[i])

    print(ans)