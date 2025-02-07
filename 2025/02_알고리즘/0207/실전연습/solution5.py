from collections import deque

F, S, G, U, D = map(int, input().split())

if S==G:
    print(0)
else :
    visited=[False]*(F+1)
    q = deque()
    q.append((0,S))
    visited[S]=True
    move = {U, -D}

    flag = False
    while q:
        cnt, item = q.popleft()
        for d in move:
            next = item+d
            if next==G:
                flag = True
                cnt += 1
                break
            if 0<next<=F and not visited[next]:
                visited[next]=True
                q.append((cnt+1,next))
        if flag: break

    if not flag:
        print("use the stairs")
    else :
        print(cnt)