arr = [['.' for _ in range(6)] for _ in range(6)]
arr[2][2]='W'
arr[3][3]='W'
arr[2][3]='B'
arr[3][2]='B'

N = int(input())
dx = [1,1,1,-1,-1,-1,0,0]
dy = [-1,1,0,-1,1,0,-1,1]

cnt = [2,2]
color = 'B'
for _ in range(N):
    x, y = map(int, input().split())
    x-=1
    y-=1
    arr[x][y]=color
    cnt[0 if color=='B' else 1] += 1

    for d in range(8):
        nx, ny = x+dx[d], y+dy[d]
        stack = []
        while (0<=nx<6 and 0<=ny<6) and arr[nx][ny]==chr(153-ord(color)):
            # 어펜드를 좌표를 바꾸고 나서 해서 오류가 발생
            stack.append((nx, ny))
            nx += dx[d]
            ny += dy[d]

        if (0<=nx<6 and 0<=ny<6) and arr[nx][ny]==color:
            cnt[0 if color == 'B' else 1] += len(stack)
            cnt[1 if color == 'B' else 0] -= len(stack)
            while stack:
                nx, ny = stack.pop()
                arr[nx][ny]=color

    color = chr(153-ord(color))

for ele in arr:
    print(''.join(ele))
print('Black' if cnt[0]>cnt[1] else 'White')


