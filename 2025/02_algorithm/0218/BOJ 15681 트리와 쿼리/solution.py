from collections import deque

N, R, Q = map(int, input().split())
adj = [[] for _ in range(N+1)]
count = [1]*(N+1)
parent = [-1]*(N+1)
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

stack =[]
stack.append(R)
pointer = 0
parent[R]=0
while pointer<len(stack):
    p = stack[pointer]
    for ele in adj[p]:
        if parent[ele]==-1:
            parent[ele]=p
            stack.append(ele)
    pointer+=1

while stack:
    n = stack.pop()
    count[parent[n]]+=count[n]

for _ in range(Q):
    print(count[int(input())])
