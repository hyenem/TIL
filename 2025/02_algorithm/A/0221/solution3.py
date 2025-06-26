# 컨베이어 벨트 움직이기
def move():
    global on
    global left
    # 컨베이어벨트 마지막칸에 선물이 있었으면
    # on(컨베이어벨트 위의 선물) 에서 하나 빼주기
    on -= arr[B-1][0]
    # 세 방향 컨베이어벨트 돌리기
    for i in range(B-1):
        arr[B-1][i]=arr[B-1][i+1]
    for i in range(B-1, 0, -1):
        arr[i][B-1]=arr[i-1][B-1]
    for i in range(B-1, 0, -1):
        arr[0][i]=arr[0][i-1]
    if left==0:
        arr[0][0]=0
    else :
        # 아직 안올라가고 남은 선물이 있으면 올리기
        # 남은 선물 하나 줄이고, 올라가있는 선물 하나 늘리고
        left-=1
        on+=1
        arr[0][0]=1


dxdy = ((1, 0), (0, 1), (-1, 0))
B, N, M = map(int, input().split())
left = M
on = 0
ans = 0
arr = [[0]*B for _ in range(B)]
# 선물을 완성하는데 남은 시간
time = [0]*N
people = []
for _ in range(N):
    x, y, t = map(int, input().split())
    people.append((x, y, t))

while left+on!=0:
    # 움직이고
    move()
    # 모든 사람을 보고
    for i in range(N):
        x, y, t = people[i]
        # 선물을 포장하는 중이면 시간 하나씩 감소(1초 지났으니까)
        if time[i]>0:
            time[i]-=1
        # 아직 선물을 다 못만들었으면 지나가기
        if time[i]!=0: continue
        # 아래, 오른쪽, 윗방향 순서(먼저 올라간 것 부터)
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<B and 0<=ny<B): continue
            # 선물이 있으면
            if arr[nx][ny]==1:
                # 컨베이어벨티위의 선물 하나 줄이고
                arr[nx][ny]=0
                on-=1
                # 정답 하나 늘리고
                ans+=1
                # 그사람의 시간 t로 만들고
                time[i]=t
                break
print(ans)