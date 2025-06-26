T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(T):
    x, y = 0,0
    d = 0
    minx, miny, maxx, maxy = 0,0,0,0
    commands=input()
    for c in commands:
        if c=='R':
            d = (d+1)%4
        elif c=='L':
            d = (d+3)%4
        elif c=='F' :
            x, y = x+dx[d], y+dy[d]
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
        else :
            x, y = x-dx[d], y-dy[d]
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
    print((maxx-minx)*(maxy-miny))