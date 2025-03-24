import heapq

T = int(input())
dxdy = ((-1, 0), (1, 0), (0, 1), (0, -1))
for _ in range(T):
    N, M = map(int,input().split())
    arr = [['.']*(M+2)] + [['.']+list(input())+['.'] for _ in range(N)] + [['.']*(M+2)]
    key = set()
    for ele in input():
        if ele=='0':break
        key.add(ord(ele)-ord('a'))
    visited = [[False]*(M+2) for _ in range(N+2)]
    visited[0][0]=True
    q = []
    heapq.heappush(q, (0, 0 ,0))
    ans = 0
    cnt = 0
    while q and cnt<len(q):
        p, x, y = heapq.heappop(q)
        if ord('A')<=ord(arr[x][y])<=ord('Z'):
            if (ord(arr[x][y])-ord('A')) not in key:
                heapq.heappush(q, (p+1, x, y))
                cnt+=1
                continue
            else :
                arr[x][y]='.'
        cnt=0
        for dx, dy in dxdy:
            if ord('A')<=ord(arr[x][y])<=ord('Z'):
                print(arr[nx][ny])
            nx = x+dx
            ny = y+dy
            if (not(0<=nx<N+2 and 0<=ny<M+2)) or visited[nx][ny] or arr[nx][ny]=='*':
                continue
            visited[nx][ny]=True
            if arr[nx][ny]=='.':
                heapq.heappush(q, (p, nx, ny))
            elif arr[nx][ny]=='$':
                ans += 1
                heapq.heappush(q, (p, nx, ny))
            elif ord('a')<=ord(arr[nx][ny])<=ord('z'):
                key.add(ord(arr[nx][ny])-ord('a'))
                heapq.heappush(q, (p, nx, ny))
            else :
                if ord(arr[nx][ny])-ord('A') in key:
                    arr[nx][ny]='.'
                    heapq.heappush(q, (p, nx, ny))
                else:
                    heapq.heappush(q, (p+1, nx, ny))
    print(ans)
