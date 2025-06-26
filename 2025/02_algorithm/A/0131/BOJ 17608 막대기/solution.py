N = int(input())
stack = []
for _ in range(N):
    data = int(input())
    #나보다 작은애는 안보이니까 pop해서 날림
    while stack:
        if stack[-1]<=data:
            stack.pop()
        else :
            break
    stack.append(data)
print(len(stack))