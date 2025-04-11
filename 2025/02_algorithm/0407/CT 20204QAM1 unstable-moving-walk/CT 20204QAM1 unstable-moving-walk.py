''' 2회독
제출횟수 : 1회
풀이시간 : 19분
'''
from collections import deque

N, K = map(int, input().split())
stable = list(map(int, input().split()))
movingwalk = deque(map(lambda x: [x, 0], stable[:N]))
movingwalk_wait = deque(stable[N:])

cnt = 0
turn = 0
while cnt<K:
    turn += 1

    s, p = movingwalk.pop()
    movingwalk_wait.appendleft(s)
    s = movingwalk_wait.pop()
    movingwalk.append([movingwalk.pop()[0], 0])
    movingwalk.appendleft([s, 0])

    for i in range(N-2, -1, -1):
        if movingwalk[i][1] and movingwalk[i+1][0] and not movingwalk[i+1][1]:
            movingwalk[i][1]=0
            movingwalk[i+1][1]=1
            movingwalk[i+1][0]-=1
            if movingwalk[i+1][0]==0:
                cnt+=1

    if movingwalk[0][0] and not movingwalk[0][1]:
        movingwalk[0]=[movingwalk[0][0]-1, 1]
        if movingwalk[0][0]==0: cnt += 1

print(turn)