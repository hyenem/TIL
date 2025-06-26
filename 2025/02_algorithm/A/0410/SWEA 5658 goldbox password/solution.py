from collections import deque

T = int(input())
dic = {'0': 0, '1':1, '2':2, '3':3, '4':4,
       '5':5, '6':6, '7':7, '8':8, '9':9,
       'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

for tc in range(1, T+1):
    N, K = map(int, input().split())
    q = deque(input())
    L = N//4
    s = set()
    for _ in range(L):
        for i in range(0, N, L):
            num = 0
            for j in range(L):
                num = num*16+dic[q[i+j]]
            s.add(num)
        q.append(q.popleft())
    l = sorted(list(s), reverse=True)
    ans = l[K-1]

    print(f'#{tc} {ans}')
