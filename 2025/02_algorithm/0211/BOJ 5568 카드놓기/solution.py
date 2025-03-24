def solution(cnt):
    global ans
    if cnt==K:
        # 중복 제거를 위해 set에 넣음
        s.add(''.join(map(str, com)))
        return
    for i in range(0, N):
        if visited[i]: continue
        visited[i]=True
        com.append(arr[i])
        solution(cnt+1)
        com.pop()
        visited[i]=False

N = int(input())
K = int(input())

fac = [1]
for i in range(1, K+1):
    fac.append(fac[-1]*i)

arr = [int(input()) for _ in range(N)]
visited = [False]*N
com = []
s = set()
solution(0)
print(len(s))