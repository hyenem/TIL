N, money, salary, G = map(int, input().split())
key = []
for _ in range(G):
    c, x = map(int, input().split())
    key.append((c, x))
kidx = 0

cnt = 0
mapp = ['S']
for _ in range(N-2):
    data = input()
    if data=='G':
        mapp.append('G')
    else:
        c, x = data.split()
        mapp.append((c, int(x)))
        cnt+=1
mapp.append('M')
for _ in range(N-2):
    data = input()
    if data=='G':
        mapp.append('G')
    else:
        c, x = data.split()
        mapp.append((c, int(x)))
        cnt+=1

mapp.append('So')
for _ in range(N-2):
    data = input()
    if data=='G':
        mapp.append('G')
    else:
        c, x = data.split()
        mapp.append((c, int(x)))
        cnt+=1

mapp.append('W')
for _ in range(N-2):
    data = input()
    if data=='G':
        mapp.append('G')
    else:
        c, x = data.split()
        mapp.append((c, int(x)))
        cnt+=1



def do(loc):
    global money, mooindo, gibu, kidx
    res = 1
    if mapp[loc]=='S' or mapp[loc]=='B':
        pass
    elif mapp[loc]=='M':
        mooindo = 3
    elif mapp[loc]=='So':
        money += gibu
        gibu = 0
    elif mapp[loc]=='W':
        if turn!=I:
            money += salary
            loc = 0
    elif mapp[loc]=='G':
        c, x = key[kidx]
        kidx = (kidx+1)%len(key)
        if c==1:
            money += x
        elif c==2:
            money -= x
            if money < 0 :
                res = 0
        elif c==3:
            gibu += x
            money -= x
            if money < 0 :
                res = 0
        elif c==4:
            loc += x
            money += (loc // (4 * N - 4)) * salary
            loc %= 4 * N - 4
            res, loc = do(loc)
    else:
        c, x = mapp[loc]
        if money>=x:
            money -= x
            mapp[loc]='B'
        else:
            res = 0
    return res, loc
I = int(input())
loc = 0
mooindo = 0
gibu = 0
turn = 0
while turn<I:
    turn+=1
    d1, d2 = map(int, input().split())

    if mooindo and d1==d2:
        mooindo = 0
        turn+=1
        d1, d2 = map(int, input().split())
    if mooindo:
        mooindo -= 1
        continue

    loc += d1+d2
    money += (loc//(4*N-4))*salary
    loc %= 4*N-4

    res, loc = do(loc)
    if not res:
        print('LOSE')
        break
else:
    if mapp.count('B')==cnt:
        print('WIN')
    else:
        print('LOSE')

