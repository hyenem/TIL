def stick():
    for x in range(N-len(sticker)+1):
        for y in range(M-len(sticker[0])+1):
            flag = 1
            for i in range(len(sticker)):
                for j in range(len(sticker[0])):
                    if arr[x+i][y+j]*sticker[i][j]==1:
                        flag = 0
                        break
                if not flag: break
            else :
                for i in range(len(sticker)):
                    for j in range(len(sticker[0])):
                        arr[x+i][y+j] += sticker[i][j]
                return True
    return False

def rotate():
    global sticker
    sticker = list(map(list, zip(*sticker)))
    sticker = [ele[::-1] for ele in sticker]

N, M, K = map(int, input().split())
stickers = []
arr = [[0]*M for _ in range(N)]
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(sticker)

for sticker in stickers:
    for i in range(4):
        res = stick()
        if res: break
        rotate()

ans = sum(map(sum, arr))
print(ans)

