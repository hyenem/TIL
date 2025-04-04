def cutter(idx):
    if idx < 0 or idx >= len(reg) or not isinstance(reg[idx], str):
        return None, None
    shape = list(reg[idx].split(':'))
    left_shape = []
    right_shape = []
    for s in shape:
        left = s[4:]
        right = s[:4]
        if left!='----':
            left_shape.append('----'+left)
        if right!='----':
            right_shape.append(right+'----')
    left_shape = ':'.join(left_shape) if left_shape else None
    right_shape = ':'.join(right_shape) if right_shape else None
    return left_shape, right_shape

def rotate(idx, angle):
    if not reg[idx]:
        return None
    shape = list(reg[idx].split(':'))
    for i in range(len(shape)):
        shape[i] = shape[i][-2*angle:]+shape[i][:-2*angle]
    return ':'.join(shape)

def combine(idx, jdx):
    if not reg[idx] or not reg[jdx]:
        return None

    shape1 = [list(ele) for ele in list(reg[idx].split(':'))]
    shape2 = list(reg[jdx].split(':'))
    lst = [4]*4
    for j in range(4):
        for i in range(len(shape2)):
            if shape2[i][j*2]!='-':
                lst[j] = i
                break

    for k in range(1, len(shape1)+1):
        for j in range(4):
            if lst[j]-k >= 0: continue
            if shape1[lst[j]-k][j*2]!='-':
                k -= 1
                break
        else : continue
        break

    for i in range(len(shape2)):
        if i>=k:
            shape1.append(shape2[i])
        else:
            for j in range(8):
                if shape2[i][j]=='-': continue
                shape1[-k+i][j]=shape2[i][j]
    shape1 = shape1[:4]
    return ':'.join([''.join(ele) for ele in shape1])

def color(idx, k):
    if not reg[idx]:
        return None

    shape = [list(ele) for ele in list(reg[idx].split(':'))]
    for i in range(len(shape)):
        for j in range(4):
            if shape[i][2*j]=='-': continue
            shape[i][2*j+1]=k
    return ':'.join([''.join(ele) for ele in shape])

reg = [None]*101
N, M = map(int, input().split())
data = [input() for _ in range(N)]
for i in range(1, N+1):
    reg[i]=data[i-1]

cmds = [tuple(input().split()) for _ in range(M)]

for c, i, j, k in cmds:
    if c=='1':
        i, j, k = map(int, (i, j, k))
        reg[j], reg[k] = cutter(i)
    elif c=='2':
        i, j, k = map(int, (i, j, k))
        reg[j] = rotate(i, k)
    elif c=='3':
        i, j, k = map(int, (i, j, k))
        reg[k] = combine(i, j)
    else:
        i, j = map(int, (i, j))
        reg[j]=color(i, k)

print(reg[100])
'''
8 4
CuCu----
----RuRu
CuCu----
--RuRu--
Ru----Ru:Ru----Ru:RuRuRuRu
--CuCu--:--CuCu--
RuRuRuRu:RuRuRuRu:RuRu----:RuRu----
----CuCu:CuCuCuCu:CuCuCuCu
3 1 2 9
3 3 4 10
3 5 6 11
3 7 8 12
'''