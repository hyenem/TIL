T = int(input())
dxdy = ((1, 0), (-1, 0), (0, -1), (0, 1))
reverse_d = (1, 0, 3, 2)
for tc in range(1, T+1):
    N = int(input())
    arr = {}
    data = [tuple(map(int, input().split())) for _ in range(N)]
    atom = []
    die = [0]*N
    for y, x, d, k in data:
        arr[(x+1000, y+1000)] = [len(atom)]
        atom.append((x+1000, y+1000, d, k))

    ans = 0
    end = 0
    while not end:
        stack = []
        end = 1
        narr = {}
        for i, (x, y, d, k) in enumerate(atom):
            if die[i]: continue

            end = 0

            dx, dy= dxdy[d]
            nx, ny = x+dx, y+dy
            if not(0<=nx<2001 and 0<=ny<2001):
                die[i]=1
                continue

            if (nx, ny) in arr:
                for ni in arr[(nx, ny)]:
                    if atom[ni][2]==reverse_d[d]:
                        die[i]=1
                        die[ni]=1
                        ans += k + atom[ni][3]
                        break
                if die[i]: continue

            if (nx, ny) not in narr: narr[(nx, ny)]=[]
            narr[(nx, ny)].append(i)
            atom[i]=(nx, ny, d, k)


        for i, (x, y, d, k) in enumerate(atom):
            if die[i]: continue

            if len(narr[(x, y)])>1:
                for idx in narr[(x, y)]:
                    die[idx]=1
                    ans += atom[idx][3]
                del narr[(x, y)]

        arr = narr

    print(f'#{tc} {ans}')
