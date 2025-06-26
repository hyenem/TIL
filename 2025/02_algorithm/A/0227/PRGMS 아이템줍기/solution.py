from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr = [[0]*52 for _ in range(52)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1+1, x2):
            for j in range(y1+1, y2):
                arr[i][j]=1
    visited = [[0]*52 for _ in range(52)]
    visited[characterX][characterY]=1
    q = deque([(0, characterX, characterY)])
    for ele in arr:
        print(ele)
    while q:
        print(q)
        c, x, y = q.popleft()
        if (x, y)==(itemX, itemY):
            answer = c
            break
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x+dx, y+dy
            if not (0<=nx<52 and 0<=ny<52): continue
            if visited[nx][ny]: continue
            if arr[nx][ny]==1: continue
            for dx, dy in ((0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0)):
                nnx, nny = nx+dx, ny+dy
                if not (0<=nnx<52 and 0<=nny<52): continue
                if arr[nnx][nny]==1:
                    visited[nx][ny]=1
                    q.append((c+1, nx, ny))
                    break
    return answer

ans = solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)
print(ans)