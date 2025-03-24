# 시작점 끝점도 연결되어야한다는 사실을 읽지않아 잠시 고전함

def solution():
    arr = []
    for _ in range(36):
        x, y = tuple(input())
        x = ord(x)-ord('A')
        y = int(y)-1
        if visited[x][y]:
            print('Invalid')
            return
        visited[x][y]=True
        if arr:
            bx, by = arr[-1]
            if (abs(bx-x), abs(by-y)) not in {(2,1), (1,2)}:
                print('Invalid')
                return
        arr.append((x,y))
    # 인덱스 오타로 한 번 틀림
    if (abs(arr[0][0]-arr[-1][0]), abs(arr[0][1]-arr[-1][1])) in {(2,1), (1,2)}:
        print('Valid')
    else : print('Invalid')


visited = [[False]*6 for _ in range(6)]
solution()