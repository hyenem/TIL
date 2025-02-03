N = int(input())
arr = list(map(int, input().split()))
stack = []
ans = [0]*N
for i in range(N):
    data = arr[i]
    while stack:
        if stack[-1][1]<=data:
            stack.pop()
        else:
            break
    if stack: ans[i]=stack[-1][0]
    stack.append((i+1, data))
print(*ans)