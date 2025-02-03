N, M = map(int, input().split())
t = int(input())
rcut = []
ccut = []
for _ in range(t):
    direc, idx = map(int, input().split())
    if direc==0:
        rcut.append(idx)
    else :
        ccut.append(idx)
rcut.sort()
ccut.sort()


rmax = M
cmax = N
if rcut: rmax = max(rcut[0], M-rcut[-1])
if ccut: cmax = max(ccut[0], N-ccut[-1])
for i in range(1, len(rcut)):
    rmax = max(rcut[i]-rcut[i-1], rmax)
for i in range(1, len(ccut)):
    cmax = max(ccut[i]-ccut[i-1], cmax)

print(rmax*cmax)