import sys
from collections import deque
sys.setrecursionlimit(10000)

def btk(i,j):
    if arr[i][j] == '$':
        dollar.append(((i, j),acc[:]))
    elif ord('a')<=ord(arr[i][j])<=ord('z'):
        key[ord(arr[i][j])-ord('a')].append(acc[:])
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        nx = i+dx
        ny = j+dy
        if not(0<=nx<N+2 and 0<=ny<M+2): continue
        if arr[nx][ny]!='*' and not visited[nx][ny]:
            visited[nx][ny]=True
            if ord('A')<=ord(arr[nx][ny])<=ord('Z'):
                acc.append(ord(arr[nx][ny])-ord('A'))
            btk(nx, ny)
            if ord('A')<=ord(arr[nx][ny])<=ord('Z'):
                acc.pop()
            if not(arr[nx][ny]=='.' or ord('A')<=ord(arr[nx][ny])<=ord('Z')):
                visited[nx][ny]=False


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [['.']*(M+2)] + [['.']+list(input())+['.'] for _ in range(N)] + [['.']*(M+2)]
    key = [[] for _ in range(26)]
    dollar = []
    acc = []
    visited = [[False]*(M+2) for _ in range(N+2)]
    visited[0][0]=True
    btk(0,0)
    keys = set()
    for ele in input():
        if ele == '0': break
        keys.add(ord(ele)-ord('a'))
    open = True
    while open:
        open=False
        for i in range(26):
            for root in key[i]:
                for ele in root:
                    if ele in keys:
                        open = True
                        root.remove(ele)
                if len(root)==0:
                    keys.add(i)

    ans = 0
    dvisited = [[False]*(M+2) for _ in range(N+2)]
    for root in dollar:
        if dvisited[root[0][0]][root[0][1]]:
            continue
        for ele in root[1]:
            if ele not in keys:
                break
        else :
            ans += 1
            dvisited[root[0][0]][root[0][1]]=True
    print(ans)

