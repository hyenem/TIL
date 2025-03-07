# 무시한다!!!
# dxdy 잘몬 만듦

direction = {'D':(1, 0), 'U': (-1, 0), 'R':(0,1), 'L': (0,-1)}
line = {'D':0, 'U':0, 'R':1, 'L':1}

N = int(input())
arr = [['.']*N for _ in range(N)]
visited = [[[False]*2 for _ in range(N)] for _ in range(N)]
x, y = 0,0
func = list(input())

for i in range(len(func)):
    d = func[i]
    nx, ny = x+direction[d][0], y+direction[d][1]
    if not (0<=nx<N and 0<=ny<N): continue
    visited[x][y][line[d]]=True
    x, y = nx, ny
    visited[x][y][line[d]] = True

for i in range(N):
    for j in range(N):
        if visited[i][j][0]:
            if visited[i][j][1]:
                arr[i][j]='+'
            else :
                arr[i][j]='|'
        elif visited[i][j][1]:
            arr[i][j]='-'

for ele in arr:
    print(''.join(ele))