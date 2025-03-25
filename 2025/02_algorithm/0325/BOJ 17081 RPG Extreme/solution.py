def move(d):
    global hero_x, hero_y
    dx, dy = dxdy[d]
    nx, ny = hero_x+dx, hero_y+dy
    if 0<=nx<N and 0<=ny<M and world[nx][ny]!='#':
        hero_x, hero_y = nx, ny

def open_box():
    T, S = box[(hero_x, hero_y)]
    if T in {'W', 'A'}:
        bag[T]=S
    else:
        if len(bag[T])<4:
            bag[T].add(S)

def trap():
    global HP
    if 'DX' in bag['O']:
        HP -= 1
    else : HP -= 5

def print_result():
    # for i in range(N):
    #     for j in range(M):
    #         if (i, j)==(hero_x, hero_y): print('@', end='')
    #         else : print(world[i][j], end='')
    #     print()
    for ele in world:
        print(''.join(ele))
    print('Passed Turns :', T+1)
    print(f'LV : {LV}')
    print(f'HP : {max(0, HP)}/{MAX_HP}')
    print(f"ATT : {ATT}+{bag['W']}")
    print(f"DEF : {DEF}+{bag['A']}")
    print(f'EXP : {EXP}/{MAX_EXP}')

def win():
    world[hero_x][hero_y] = '@'
    print_result()
    print('YOU WIN!')

def draw():
    world[hero_x][hero_y]='@'
    print_result()
    print('Press any key to continue.')
def die(word):
    if HP<=0:
        if 'RE' not in bag['O']:
            print_result()
            print(f'YOU HAVE BEEN KILLED BY {word}..')
            return 1
        else:
            RE()
            return 0
    return 0

def level_up():
    global LV, MAX_HP, ATT, DEF, HP, EXP, MAX_EXP
    LV += 1
    MAX_HP, ATT, DEF = MAX_HP+5, ATT+2, DEF+2
    HP = MAX_HP
    EXP, MAX_EXP = 0, 5*LV

def kill(E):
    global EXP
    if 'HR' in bag['O']:
        HR()
    world[hero_x][hero_y]='.'
    rE = E
    if 'EX' in bag['O']:
        rE = (rE*6)//5
    EXP += rE
    if EXP >= MAX_EXP:
        level_up()
def fight():
    global HP

    mS, mW, mA, mH, mE = monsters[(hero_x, hero_y)]
    rATT, rDEF = ATT+bag['W'], DEF+bag['A']

    if 'CO' in bag['O']:
        if 'DX' in bag['O']:
            fATT = rATT*3
        else: fATT = rATT*2
    else : fATT = rATT

    if world[hero_x][hero_y]=='M' and 'HU' in bag['O']:
        HP = MAX_HP
        mH -= max(1, fATT-mA)
        if mH<=0:
            kill(mE)
            return 1

    else :
        mH -= max(1, fATT - mA)
        if mH <= 0:
            kill(mE)
            return 1

        HP -= max(1, mW - rDEF)
        if HP <= 0:
            if die(mS):
                return 0
            else:
                return 2

    while True:
        mH -= max(1, rATT - mA)
        if mH<=0:
            kill(mE)
            return 1

        HP -= max(1, mW - rDEF)
        if HP <= 0:
            if die(mS):
                return 0
            else:
                return 2


def HR():
    global HP
    HP = min(MAX_HP, HP+3)

def RE():
    global HP, hero_x, hero_y
    bag['O'].remove('RE')
    HP = MAX_HP
    hero_x, hero_y = start_x, start_y


N, M = map(int, input().split())
world = [list(input()) for _ in range(N)]
K, L = 0, 0
for i in range(N):
    for j in range(M):
        if world[i][j]=='@':
            hero_x, hero_y = i, j
            start_x, start_y = i, j
            world[i][j]='.'
        elif world[i][j] in {'&', 'M'}:
            K += 1
        elif world[i][j] == 'B':
            L += 1

cmds = list(input())
dxdy = {'U':(-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

mdata = [tuple(input().split()) for _ in range(K)]
monsters = {}
for R, C, S, W, A, H, E in mdata:
    monsters[(int(R)-1, int(C)-1)]=(S, int(W), int(A), int(H), int(E))

bdata = [tuple(input().split()) for _ in range(L)]
box = {}
for R, C, T, S in bdata:
    if T in {'W', 'A'}:
        box[(int(R)-1, int(C)-1)] = (T, int(S))
    else :
        box[(int(R)-1, int(C)-1)] = (T, S)

bag = {'W': 0, 'A': 0, 'O': set()}

LV = 1
HP, MAX_HP = 20, 20
ATT = 2
DEF = 2
EXP, MAX_EXP = 0, 5

for T in range(len(cmds)):
    move(cmds[T])

    todo = world[hero_x][hero_y]
    if todo =='B':
        world[hero_x][hero_y]='.'
        open_box()
    elif todo=='^':
        trap()
        if die('SPIKE TRAP'): break

    elif todo=='&':
        alive = fight()
        if not alive:
            break

    elif todo=='M':
        alive = fight()
        if not alive: break
        elif alive==1:
            win()
            break
    # print(cmds[T])
    # print_result()
    # print('---------------------------')
else :
    draw()


