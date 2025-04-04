def my_print():
    for b_num in range(1, M+1):
        print(f'belt{b_num}', end=': ')
        b_head = head[b_num]
        if b_head==-1: continue

        b_belt = belts[b_num]
        id, w = belts[b_num][b_head][0], gifts[belts[b_num][b_head][0]][0]
        print(id, w, end=', ')
        now = belts[b_num][b_head][2]
        while now != head[b_num]:
            id, left, right = b_belt[now]
            w = gifts[id][0]
            print(id, w, end=', ')
            now = right
        print()
    print('---------------------------------')

def init():
    global N, M, belts, head, gifts
    N, M = data[1:3]
    ID_data = data[3:3 + N]
    W_data = data[3 + N:]
    belts = [0] * (M + 1)
    head = [0]*(M+1)

    gifts = {}
    for i in range(M):
        belt = []
        for j in range(N//M):
            gifts[ID_data[i*(N//M)+j]] = (W_data[i*(N//M)+j], i+1, j)
            belt.append([ID_data[i*(N//M)+j], (j-1)%(N//M), (j+1)%(N//M)])
        belts[i+1]=belt

def down(w_max):
    res = 0
    for b_num in range(1, M+1):
        b_head = head[b_num]
        if b_head == -1: continue

        id = belts[b_num][b_head][0]
        if gifts[id][0]<=w_max:
            res+=gifts[id][0]

            left = belts[b_num][b_head][1]
            right = belts[b_num][b_head][2]
            belts[b_num][left][2] = right
            belts[b_num][right][1] = left
            head[b_num] = right
            del gifts[id]
        else:
            head[b_num]=belts[b_num][b_head][2]
    print(res)

def remove(r_id):
    if r_id not in gifts:
        print(-1)
        return

    w, b_num, b_idx = gifts[r_id]
    del gifts[r_id]

    left = belts[b_num][b_idx][1]
    right = belts[b_num][b_idx][2]
    belts[b_num][left][2] = right
    belts[b_num][right][1] = left
    if b_idx==head[b_num]:
        head[b_num]=right

    print(r_id)

def find(f_id):
    if f_id not in gifts:
        print(-1)
        return

    w, b_num, b_idx = gifts[f_id]
    head[b_num]=b_idx
    print(b_num)

def break_belt(b_num):
    if head[b_num]==-1:
        print(-1)
        return

    for k in range(1, M):
        if head[(b_num-1+k)%M+1]!=-1:
            next_b_num = (b_num-1+k)%M+1
            break

    next_belt = belts[next_b_num]
    next_head = head[next_b_num]
    next_tail = next_belt[next_head][1]

    next_belt[next_tail][2]=len(next_belt)

    b_belt = belts[b_num]
    now = head[b_num]
    id, left, right = b_belt[now]
    w, _, _ = gifts[id]
    gifts[id]=(w, next_b_num, len(next_belt))
    belts[next_b_num].append([id, next_tail, len(next_belt)+1])

    now = right
    while now!=head[b_num]:
        id, left, right = b_belt[now]
        w, _, _ = gifts[id]
        gifts[id] = (w, next_b_num, len(next_belt))
        belts[next_b_num].append([id, len(next_belt)-1, len(next_belt) + 1])
        now = right
    next_belt[-1][2]=next_head

    next_belt[next_head][1]=len(next_belt)-1

    head[b_num]=-1
    belts[b_num]=[]

    print(b_num)


Q = int(input())
cmds = [list(map(int, input().split())) for _ in range(Q)]

for data in cmds:
    if data[0]==100:
        init()
    elif data[0]==200:
        w_max = data[1]
        down(w_max)
    elif data[0]==300:
        r_id = data[1]
        remove(r_id)
    elif data[0]==400:
        f_id = data[1]
        find(f_id)
    else:
        b_num=data[1]
        break_belt(b_num)
    # my_print()