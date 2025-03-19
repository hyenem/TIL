N, K = map(int, input().split())
root = list(input())
plants = [tuple(map(int, input().split())) for _ in range(N)]
x, y = plants.pop(0)
plants.sort()

summ = {}
subb = {}
visited = set()

for i in range(N-1):
    px, py = plants[i]
    if px+py not in summ: summ[px+py] = []
    if px-py not in subb: subb[px-py] = []
    summ[px+py].append((px, py))
    subb[px-py].append((px, py))


for r in root:
    if r == 'A':
        lst = subb[x - y]
        i = 0
        while i<len(lst):
            if lst[i][0] > x:
                nx, ny = lst[i]
                if (nx, ny) in visited:
                    del lst[i]
                    continue
                x, y = nx, ny
                visited.add((nx, ny))
                del lst[i]
                break
            i += 1
    elif r == 'B':
        lst = summ[x + y]
        i = 0
        while i < len(lst):
            if lst[i][0] > x:
                nx, ny = lst[i]
                if (nx, ny) in visited:
                    del lst[i]
                    continue
                x, y = nx, ny
                visited.add((nx, ny))
                del lst[i]
                break
            i += 1
    elif r=='C' :
        lst = summ[x+y]
        i = len(lst)-1
        while i>=0:
            if lst[i][0] < x:
                nx, ny = lst[i]
                if (nx, ny) in visited:
                    del lst[i]
                    i-=1
                    continue
                x, y = nx, ny
                visited.add((nx, ny))
                del lst[i]
                break
            i -= 1
    else :
        lst = subb[x-y]
        i = len(lst)-1
        while i>=0:
            if lst[i][0] < x:
                nx, ny = lst[i]
                if (nx, ny) in visited:
                    del lst[i]
                    i-=1
                    continue
                x, y = nx, ny
                visited.add((nx, ny))
                del lst[i]
                break
            i -= 1

print(x, y)