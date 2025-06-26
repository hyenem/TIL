# 왼쪽, 오른쪽 위아래 바꼈으때도 그대로 되는지 확인해야지
# x, y 좌표 순서도 헷갈리지 말아야지

def solution():
    global x, y
    d = 0
    for _ in range(K):
        func, n = input().split()
        n = int(n)
        if func=='MOVE':
            x+=dxdy[d][0]*n
            y+=dxdy[d][1]*n
            if not(0<=x<=N and 0<=y<=N):
                return False
        else :
            if n==0:
                d=(d+1)%4
            else :
                d=(d-1)%4
    return True


N, K = map(int, input().split())
dxdy = ((0,1), (1,0), (0, -1), (-1, 0))
x, y = 0,0

if solution():
    print(y, x)
else :
    print(-1)
