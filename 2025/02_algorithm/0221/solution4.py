# 문제 차근히 읽고 할일 정리하기
# 조건을 너무 많이 빼먹음
# N에서 로봇이 빠져나간다는 것도,,,
# 방문 배열 같이 안돌린것도,,,,,

from collections import deque

N, K = map(int, input().split())
q = deque(map(int, input().split()))
# 로봇의 좌표
robot = []
# 로봇이 있으면 True 없으면 False
robotv = deque([False]*(2*N))
ans = 0

# 이미 내구도가 0이면 처리해주기
for ele in q:
    if ele==0: K-=1

while K>0:
    ans += 1

    # 컨베이어벨트 돌리기
    q.appendleft(q.pop())
    robotv.appendleft(robotv.pop())
    for i in range(len(robot)):
        robot[i] = (robot[i]+1)%(2*N)
    # 돌아갔는데 로봇 나갈 수 있으면
    for i in range(len(robot)):
        if robot[i]==N-1:
            # 로봇 있다는 표시 False 로 만들고
            robotv[robot[i]]=False
            # 로봇 나가기
            del robot[i]
            break

    # 이동할 수 있는 로봇 이동하기
    for i in range(len(robot)):
        x = robot[i]
        nx = (x+1)%(2*N)
        # 다음칸에 로봇 있으면 못간다
        if robotv[nx]: continue
        # 다음칸 로봇 없고 내구도 0아니면
        if q[nx]!=0:
            # 내구도 줄여주고
            q[nx]-=1
            if q[nx]==0: K-=1
            # 로봇 방문표시 옮기고, 로봇 좌표 옮기고
            robotv[x]=False
            robotv[nx]=True
            robot[i]=nx
    # 옮기고 나서 나갈 수 있는 로봇 있으면 내보내기
    for i in range(len(robot)):
        if robot[i]==N-1:
            robotv[robot[i]] = False
            del robot[i]
            break

    # 첫번째 칸에 로봇 놓기
    # 이미 로봇이 있거나 내구도가 0인경우는 그냥 지나가기
    if q[0]!=0 and not robotv[0]:
        robot.append(0)
        robotv[0]=True
        q[0]-=1
        if q[0]==0: K-=1

print(ans)
