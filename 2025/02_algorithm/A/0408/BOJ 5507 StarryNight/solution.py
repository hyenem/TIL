W, H = int(input()), int(input())
arr = [list(map(int, input())) for _ in range(H)]
ans = [['0']*W for _ in range(H)]
dxdy = ((-1, 0), (-1, 1), (-1, -1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
clusters = []
for i in range(H):
    for j in range(W):
        if arr[i][j]==0: continue

        minx, maxx, miny, maxy = i, i, j, j
        q = [(i, j)]
        idx = 0
        arr[i][j]=0

        while idx<len(q):
            x, y = q[idx]
            minx, maxx = min(minx, x), max(maxx, x)
            miny, maxy = min(miny, y), max(maxy, y)
            idx += 1
            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if not(0<=nx<H and 0<=ny<W): continue
                if arr[nx][ny]==0: continue
                q.append((nx, ny))
                arr[nx][ny]=0

        cluster = [[0]*(maxy-miny+1) for _ in range(maxx-minx+1)]
        for x, y in q:
            cluster[x-minx][y-miny]=1

        for k in range(len(clusters)):
            c = clusters[k]
            for r in range(8):
                if len(c)==len(cluster) and len(c[0])==len(cluster[0]):
                    for ni in range(len(cluster)):
                        for nj in range(len(cluster[0])):
                            if c[ni][nj]!=cluster[ni][nj]:
                                break
                        else: continue
                        break
                    else:
                        s = chr(ord('a')+k)
                        for x, y in q:
                            ans[x][y]=s
                        break
                cluster = list(map(list, zip(*cluster[::-1])))
                if r==3:
                    cluster = cluster[::-1]
            else: continue
            break
        else:
            s = chr(ord('a') + len(clusters))
            for x, y in q:
                ans[x][y] = s
            clusters.append(cluster)

for ele in ans:
    print(''.join(ele))