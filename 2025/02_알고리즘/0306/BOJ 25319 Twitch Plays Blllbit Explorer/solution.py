from collections import deque

def goto(nx, ny):
    if x<nx:
        ans.append('D'*(nx-x))
    else :
        ans.append('U'*(x-nx))

    if y<ny:
        ans.append('R'*(ny-y))
    else :
        ans.append('L'*(y-ny))

N, M, S = map(int, input().split())
arr = [list(input()) for _ in range(N)]
cnt = [0]*26
loc = [deque() for _ in range(26)]
ans = []
id = list(map(lambda x: ord(x)-ord('a'), input()))
for i in range(N):
    for j in range(M):
        loc[ord(arr[i][j])-ord('a')].append((i, j))
        cnt[ord(arr[i][j])-ord('a')]+=1


C = 0
x, y = 0, 0
end = 0
while True:
    for ele in id:
        cnt[ele]-= 1
        if cnt[ele]<0:
            goto(N-1, M-1)
            end = 1
            break
    if end : break

    for ele in id :
        nx, ny = loc[ele].popleft()
        goto(nx, ny)
        x, y = nx, ny
        ans.append('P')
    C += 1

strans = ''.join(ans)
print(C, len(strans))
print(strans)