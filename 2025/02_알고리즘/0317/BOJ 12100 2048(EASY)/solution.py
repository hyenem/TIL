'''
제출횟수 : 4회
풀이시간 : 1시간 40분

실행시간 : 140ms
메모리 : 111928KB


[오해한 것]
>> 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다.
>> 입력이 아니라 이동 후에도 블럭이 1024보다 클 수 없다고 생각
어케 그러냐고 ㅋㅋㅋㅋ큐ㅜㅠㅜㅠㅜㅜㅠㅜㅠㅜㅠㅜ
애초에 문제 이름이 2048인데 ㅋㅋ큐ㅜㅠㅜㅠ 1024에서 참이나 끝나겠다ㅠㅜㅠㅜㅠ
그냥 나가죽자,,,,,,,, 머리박고 ㅋㅋ쿠ㅠㅜㅠㅜㅠㅠㅠㅜㅠㅠㅜㅠㅜㅜ


[시간복잡도]
재귀호출수 * 시행횟수 * 배열복사 * 블럭처리
4^5 * N^2 * N^2
1024 * N^4
최악 : 40960000

[엣지케이스] : 백준에 없는 엣지케이스(해당케이스 검증 못하는 코드가 통과됨)
7
32 16 8 4 2 2 2
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
정답 : 64
오답코드 : 32

구상 : 5분
* 0이 자리를 잡고있으면 오히려 힘들 것 같은데
* 그냥 del 처리하고, del하면 내려가는게 움직이는 방향되도록 회전해서 처리하자

구현 : 25분
* 0인 부분을 처음에 지우고 시작하려고 했는데,
* 돌리는 방향마다 지우면 상태가 달라서(지우고 돌리기-> 돌리고 지우기 다름)
* 모든 방향에 대해서 처음 돌릴때 지워주는 방식으로 바꿈

디버깅 : 1시간 10분
* 구현이후 openTC 모두 정답 -> 제출
    -> 틀렸습니다.
* 열의 크기들이 행마다 다를때 zip으로 전치하면 이상하게 나온다는 걸 깨닫고 수정
    -> 틀렸습니다.
* 회전하고 tmp를 구한뒤에 상을 처리하고, tmp를 ::-1 해서 하를 처리했는데,
    이미 상을 처리하면서 tmp는 바뀌어있었음,,
    -> tmp 받으면서 ttmp 도 같이 받아서 제대로 된 배열로 하를 처리함
    -> 틀렸습니다
* 1024가 시작의 상한이라는걸,,,깨달음,,,, ans==1024 return 다 없앰
    -> 맞았습니다.

리펙토링
* 코드 작성 중 좌로 가는 것은 이전 방향의 반복이므로
* 가지치기 가능할 것이라고 생각
* 해당 부분을 pop함수의 변화 개수를 받아서 가지치기함

'''

def delete(tmp):
    for i in range(len(tmp)):
        for j in range(len(tmp[i])-1, -1, -1):
            if tmp[i][j]==0:
                del tmp[i][j]

def pop(tmp):
    global ans
    cnt = 0
    for i in range(len(tmp)):
        idx = 0
        while idx < len(tmp[i]) - 1:
            if tmp[i][idx] == tmp[i][idx + 1]:
                tmp[i][idx] *= 2
                cnt +=1
                ans = max(tmp[i][idx], ans)

                del tmp[i][idx + 1]
            idx += 1
    return cnt

def btk(cnt, arr):
    if cnt==5: return

    # 좌
    tmp = [ele[:] for ele in arr]
    if cnt==0:
        delete(tmp)
    cango = pop(tmp)
    if cnt==0 or (cnt!=0 and cango):
        btk(cnt+1, tmp)

    # 우
    tmp = [ele[::-1] for ele in arr]
    if cnt==0:
        delete(tmp)
    pop(tmp)
    btk(cnt+1, tmp)

    # 상
    tmp = [[] for _ in range(N)]
    ttmp = [[] for _ in range(N)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            tmp[j].append(arr[i][j])
            ttmp[j].append(arr[i][j])
    if cnt==0:
        delete(tmp)
    pop(tmp)
    btk(cnt+1, tmp)

    # 하
    tmp = [ele[::-1] for ele in ttmp]
    if cnt==0:
        delete(tmp)
    pop(tmp)
    btk(cnt+1, tmp)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, arr[i][j])
btk(0, arr)

print(ans)