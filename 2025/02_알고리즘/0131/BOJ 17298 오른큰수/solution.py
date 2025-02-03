N = int(input())
data = list(map(int, input().split()))
ans = [-1]*N
stack = []
for i in range(N):
    while stack:
        if stack[-1][1]<data[i]:
            tmp = stack.pop()
            ans[tmp[0]]=data[i]
        else :
            break
    stack.append([i, data[i]])
print(*ans)