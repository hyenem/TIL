def modok():
    end = 0
    mminus, eminus = 0, 0
    while not end:
        end = 1
        for i in range(N):
            if me[i][1]==0: continue
            me[i][1]-=1
            if me[i][1]==0:
                end = 0
                mminus += 1
        for i in range(M):
            if enemy[i][1]==0: continue
            enemy[i][1]-=1
            if enemy[i][1]==0:
                end = 0
                eminus += 1
    return mminus, eminus

def btk(idx, use_modok, last_attack, mcnt, ecnt):
    global me, enemy

    if ecnt==0: return True

    if use_modok and mcnt<ecnt: return False

    if last_attack!=-1 and enemy[last_attack][1]!=0:
        for n in range(N):
            if visited[n] or me[n][1] == 0: continue

            mminus, eminus = 0, 0
            mhp, ehp = me[n][1], enemy[last_attack][1]

            visited[n] = 1
            me[n][1] = max(0, me[n][1] - enemy[last_attack][0])
            enemy[last_attack][1] = max(0, enemy[last_attack][1] - me[n][0])
            if me[n][1]==0: mminus = 1
            if enemy[last_attack][1]==0: eminus = 1
            attack.append((n + 1, last_attack + 1))

            if btk(n + 1, use_modok, last_attack, mcnt-mminus, ecnt-eminus):
                return True

            attack.pop()
            visited[n] = 0
            me[n][1], enemy[last_attack][1] = mhp, ehp


    if not use_modok:
        me_tmp = [ele[:] for ele in me]
        enemy_tmp = [ele[:] for ele in enemy]
        mminus, eminus = modok()
        attack.append((-1, -1))
        if btk(0, 1, -1, mcnt-mminus, ecnt-eminus):
            return True
        attack.pop()
        me, enemy = me_tmp, enemy_tmp

    for n in range(idx, N):
        if visited[n] or me[n][1]==0: continue

        for m in range(M):
            if enemy[m][1]==0: continue

            mminus, eminus = 0, 0
            mhp, ehp = me[n][1], enemy[m][1]

            visited[n]=1
            me[n][1] = max(0, me[n][1]-enemy[m][0])
            enemy[m][1] = max(0, enemy[m][1]-me[n][0])
            if me[n][1]==0: mminus = 1
            if enemy[m][1]==0: eminus = 1
            attack.append((n+1, m+1))

            if btk(n+1, use_modok, m, mcnt-mminus, ecnt-eminus):
                return True

            attack.pop()
            visited[n]=0
            me[n][1], enemy[m][1] = mhp, ehp

    return False

N, M = map(int, input().split())
me = [list(map(int, input().split())) for _ in range(N)]
enemy = [list(map(int, input().split())) for _ in range(M)]
visited =[0]*N
attack = []
res = btk(0, 0, -1, N, M)
if res:
    print(len(attack))
    for n, m in attack:
        if n==-1:
            print('use modok')
        else: print(f'attack {n} {m}')
else:
    print(-1)