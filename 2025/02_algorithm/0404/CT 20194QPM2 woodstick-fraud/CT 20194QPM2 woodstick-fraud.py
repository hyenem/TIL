'''2회독
제출횟수 : 1회
풀이시간 : 23분

* 문제조건 빼먹지 말것!
* 별다른 피드백 없음

'''

def btk(idx, acc):
    global ans
    if idx==len(lst):
        ans = max(ans, acc)
        return

    for i in range(4):
        if horse[i]==-1: continue
        tmp = horse[i]
        if horse[i]<20 and horse[i] not in {5, 10, 15}:
            horse[i]+=lst[idx]
            if horse[i]>20:
                horse[i]=-1
        else:
            for _ in range(lst[idx]):
                horse[i]=move[horse[i]]
                if horse[i]==-1:
                    break
        if horse[i]!=-1 and horse.count(horse[i])>=2:
            horse[i]=tmp
            continue

        if horse[i]!=-1:
            btk(idx+1, acc+score[horse[i]])
        else:
            btk(idx+1, acc)

        horse[i]=tmp


score = [2*i for i in range(21)]+[13, 16, 19]+[22, 24]+[28, 27, 26]+[25, 30, 35]
move = [i for i in range(1, 21)]+[-1]+[22, 23, 29]+[25, 29]+[27, 28, 29]+[30, 31, 20]
move[5]=21
move[10]=24
move[15]=26

lst = list(map(int, input().split()))
horse = [0]*4
ans = 0
btk(0, 0)
print(ans)

'''
제출횟수 : 1회
풀이시간 : 54분

실행시간 : 160ms -> 108ms
메모리 : 111640KB

[ 오해한 점 ]
40을 중복 방문 가능하다고 생각함

구상 : 10분
* 문제 형태를 보고 우선 당황함
* 노드를 만들어야하나 조건문을 걸어야하나 어째야하나 고민하다가
* 링크드 리스트 생각나서 다음 노드 인덱스 표시하는 테이블로 가기로 함

구현 : 17분
* 룩업테이블 만드는데 시간이 많이 소요됨
* 미리 인덱스대로 종이에 그려놓고 했으면 훨씬 빨랐을텐데

디버깅 : 27분
[1] 0인 경우에도 move가 아니라 인덱스를 더해주는 구조로 가게 했어야했는데
    조건문을 잘 못 걸어서 0인 경우 move로 이동 -> 계속 제자리
[2] 오픈테케 답이 이상하게 나와서 한참 들여다봄
    40(인덱스 20)을 도착 지점처럼 다뤘었는데, 사실 40에서는 중복 방문이 안됨
    도착 지점을 20으로 지정하는게 아니라 -1로 지정함
[3] 혹시 몰라서 최댓값 가지치기하고 제출

리팩토링
[1] 말끼리 서로 구분이 안되자나? 같은 좌표(0)에 있는 말은 하나만 옮겨보면 되자나?
        if i!=0 and loc[i-1]==loc[i]:
            break

[ 시간복잡도 ]
중복순열
4^10 == 2^20 문제없음

[ 엣지케이스 ] : 이건 문제 조건에 맞는 엣지케이스는 아닌데, 말 하나로 돌렸을 때 잘 가고있는지 채크 가능
3 3 1 1 1 1 1 1 1 1
6 4 1 1 1 1 1 1 1 1
10 1 1 1 1 1 1 1 1 1
4 4 4 3 1 1 1 1 1 1
15 1 1 1 1 1 1 1 1 1
4 4 4 4 1 1 1 1 1 1


def btk(idx, acc):
    global ans
    # 가지치기
    # 남은 칸 다 가도 최댓값보다 작으면 그만하기
    if (10 - idx) * 40 + acc <= ans: return

    # 주사위 다 굴리면 정답 갱신
    if idx == 10:
        ans = max(ans, acc)
        return

    for i in range(4):
        # 도착했으면 움직이지 않음
        if loc[i] == -1:
            continue
        # 어차피 말끼리는 구분이 안되기 때문에 위치가 같은 말을 여러번 바꿔볼 필요가 없어
        # 근데 인제 위치가 같을 수 있는 경우는 0 뿐이기 때문에?
        # 한번 0이 나오면 뒤로도 쭉 0이니까 break 해도 되지 않을까?
        if i!=0 and loc[i-1]==loc[i]:
            break

        # btk을 위해 이전 위치 저장
        tmp = loc[i]

        # 한번도 파란길을 타지 않고 빨간 길을 따라가야하는 경우
        if (loc[i] < 20 and loc[i] % 5 != 0) or loc[i] == 0:
            loc[i] += arr[idx]
            # 도착한 경우 -1
            if loc[i] > 20:
                loc[i] = -1
        # 파란길을 한 번이라도 탔거나 이번에 타야하는 경우
        else:
            # move 테이블을 통해서 이동함ㅁ
            for _ in range(arr[idx]):
                loc[i] = move[loc[i]]
                # 도착한 경우 멈추기
                if loc[i] == -1: break

        # 갈 수 있는지 확인(다른 말 중에 좌표가 같은 말이 있나?)
        for j in range(4):
            if i == j: continue
            if loc[i] == loc[j] and loc[i] != -1:
                break
        else:
            # 갈 수 있으면 보내기
            # 근데 인제 도착했으면 점수 추가 없음
            if loc[i] != -1:
                btk(idx + 1, acc + score[loc[i]])
            else:
                btk(idx + 1, acc)

        loc[i] = tmp


# 해당 칸에 갔을 때 다음에 어디로 가야하는가?
move = [i for i in range(21)] + [22, 23, 24, 25, 26, 20] + [28, 24] + [30, 31, 24]
move[20] = -1
move[5] = 21
move[10] = 27
move[15] = 29
# 각 칸의 점수
score = [2 * i for i in range(21)] + [13, 16, 19, 25, 30, 35] + [22, 24] + [28, 27, 26]

loc = [0] * 4
arr = list(map(int, input().split()))
ans = 0
btk(0, 0)
print(ans)
'''