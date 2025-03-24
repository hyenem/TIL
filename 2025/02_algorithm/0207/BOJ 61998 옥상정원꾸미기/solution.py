N = int(input())
stack = []
ans = 0
for _ in range(N):
    data = int(input())
    if stack and stack[-1]<=data:
        while stack and stack[-1]<=data:
            stack.pop()
            ans+=len(stack)
    stack.append(data)

while stack:
    stack.pop()
    ans += len(stack)
print(ans)