def star(x, y, n):
    if n==3:
        arr[x][y+2]='*'
        arr[x+1][y+1]='*'
        arr[x+1][y+3]='*'
        arr[x+2][y]='*'
        arr[x+2][y+1]='*'
        arr[x+2][y+2]='*'
        arr[x+2][y+3]='*'
        arr[x+2][y+4]='*'
        return
    star(x, y+n//2, n//2)
    star(x+n//2, y, n//2)
    star(x+n//2, y+n, n//2)

N = int(input())
arr = [[' ']*(2*N) for _ in range(N)]
star(0, 0, N)
for ele in arr:
    print(''.join(ele))
