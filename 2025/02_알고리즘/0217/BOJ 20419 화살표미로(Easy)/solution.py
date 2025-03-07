def solution(x, y, l, r):
    if x==R-1 and y==C-1:
        return True
    thisd = direction[arr[x][y]]
    for d in range(4):
        nx, ny = x+dxdy[d][0], y+dxdy[d][1]
        if not(0<=nx<R and 0<=ny<C) or visited[nx][ny]: continue
        if d==thisd:
            visited[nx][ny]=True
            if solution(nx, ny, l, r): return True
            visited[nx][ny]=False
        else :
            rdist = (d-thisd+4)%4
            if r>=rdist:
                visited[nx][ny]=True
                if solution(nx, ny, l, r-rdist): return True
                visited[nx][ny]=False
            if l>=4-rdist:
                visited[nx][ny]=True
                if solution(nx, ny, l-4+rdist, r): return True
                visited[nx][ny]=False
    return False

direction ={'U':0, 'D':2, 'L':3, 'R':1}
dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
visited[0][0]=True
if solution(0,0,K, K):
    print('Yes')
else:
    print('No')


