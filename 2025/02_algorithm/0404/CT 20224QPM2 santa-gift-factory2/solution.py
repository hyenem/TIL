def init(lst):
    global N, M, belts, gifts, cnt
    N, M = lst[0], lst[1]
    belts = [[] for _ in range(1, N)]
    head = [-1]*(N+1)
    tail = [-1]*(N+1)
    cnt = [0]*(N+1)
    gifts = [0]
    for i in range(1, M+1):
        num = lst[i+1]
        cnt[num]+=1

        if head[num]==-1:
            head[num]=i
            tail[num]=i
            gifts.append([-1, -1])
        else:
            tail[num]=i
            gifts[tail[num]][1]=i
            gifts.append([tail[num], -1])

def move(src, dst):
    sh, st = belts[src]
    dh, dt = belts[dst]
    gifts[dt][1]=sh
    gifts[sh][0]=dt
    belts[dst][1]=st
    belts[src]=[-1, -1]
    cnt[dst]+=cnt[src]
    cnt[src]=0
    print(cnt[dst])

def move_front(src, dst):
    if cnt[src]==0 and cnt[dst]==0:
        print(cnt[dst])
    elif cnt[src]==0:
        cnt[src]+=1
        cnt[dst]-=1
        dh = belts[0]

        print(cnt[dst])
    elif cnt[dst]==0:

    else:

Q = int(input())
request = [list(map(int, input().split())) for _ in range(Q)]
for rq in request:
    if rq[0]==100:
        init(rq[1:])
    elif rq[0]==200:
        m_src, m_dst = rq[1], rq[2]
        move(m_src, m_dst)
    elif rq[0]==300:
        m_src, m_dst = rq[1], rq[2]
        move_front(m_src, m_dst)