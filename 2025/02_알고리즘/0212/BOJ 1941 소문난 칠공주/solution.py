def solution(cntS, cnt, visited):
    global ans
    # 추가되어야하는 S의 개수가 남은 수보다 크면 달성불가
    if 4-cntS > 7-cnt:
        return
    if cnt==7:
        if cntS>=4:
            ans.add(visited)
        return
    #내가 왔던 모든 칸에 대해서
    for ele in s:
        x, y = ele
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<5 and 0<=ny<5): continue
            if visited&(1<<(5*nx+ny)): continue
            s.add((nx, ny))
            if arr[nx][ny]=='S':
                # 한 칸 먹고 다음 칸으로 넘어가기
                solution(cntS+1, cnt+1, visited|(1<<(5*nx+ny)))
            else :
                solution(cntS, cnt+1, visited|(1<<(5*nx+ny)))
            s.remove((nx, ny))

dxdy =((-1, 0), (1, 0), (0, -1), (0, 1))
arr = [list(input()) for _ in range(5)]
ans = set()
for i in range(5):
    for j in range(5):
        if arr[i][j]=='S':
            # 한번 포함된 S는 방문처리안하면
            # 중복으로 계산됨
            s = {(i,j)}
            solution(1, 1, 1<<(5*i+j))


print(len(ans))