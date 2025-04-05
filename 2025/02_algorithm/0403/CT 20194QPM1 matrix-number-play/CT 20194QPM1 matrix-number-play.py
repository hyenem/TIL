'''2회독
제출횟수 : 1회
풀이시간 : 25분

* 인덱스 OOB 혼자 생각해서 채크한거 아주 잘했서~
* 한번 돌리기 전에도 채크하는 것도 잘했서~~
* 크게 피드백할 것 없음
'''

def sort():
    maxcol = 0
    for i in range(len(arr)):
        row = arr[i]

        row.sort()
        newrow = []
        for j in range(len(row)):
            if row[j]==0: continue
            if newrow and newrow[-1][1]==row[j]:
                newrow[-1][0]+=1
            else:
                newrow.append([1, row[j]])
        newrow.sort()

        arr[i] = []
        for ele in newrow:
            arr[i]+=[ele[1], ele[0]]
        arr[i]=arr[i][:100]
        maxcol = max(maxcol, len(arr[i]))

    for i in range(len(arr)):
        if len(arr[i])<maxcol:
            arr[i].extend([0]*(maxcol-len(arr[i])))



R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

for time in range(0, 101):
    if 0<=R-1<len(arr) and 0<=C-1<len(arr[0]) and arr[R-1][C-1]==K:
        print(time)
        break

    if len(arr)>=len(arr[0]):
        sort()
    else:
        arr = list(map(list, zip(*arr)))
        sort()
        arr = list(map(list, zip(*arr)))
else :
    print(-1)

'''
제출횟수 : 3회
>> 1차 : while 문의 종료조건을 잘못 걸어서 t=0일때를 못잡음
        : tc1 한이 번 더 넣어봤어도 안생겼을 문데,,,
>> 2차 : r, c가 배열의 크기보다 클 떄도 있다는 사실을 간과함
        : 이미 알고있던 사실었는데, 초기조건은,,, 안그럴거라고생각,,
풀이시간 : 41분

실행시간 : 124ms
메모리 : 111476KB

! 명심할 것 !
문제 그대로 구현할게 아니라면,
내가 변형한 것 때문에 야기되는 문제가 없는지 다시 한 번 확인할 것
>> 전치를 했다가 다시 돌리기 보다는 한 번 하고 말았는데
>> 정사각행렬일때 전치 여부가 바뀐다는 사실을 간과함
>> 수정 전
        if N<M:
            arr = list(zip(*arr))
            r, c = c, r
>> 수정 후
        if N<M or (N==M and t):
            arr = list(zip(*arr))
            r, c = c, r
            t = 1-t

구상 : 5분
* 개수를 세고, 정렬해주는 방법에 대해 고민함
* 방법1) 배열의 인덱스로 접근해서 세주고, 0인 애들 제외하고 list에 넣어서 정렬
* 방법2) dict로 어떤 수가 몇번 인덱스인지 관리해주기
* 방법 2로 가기로함

구현 : 10분
디버깅 : 26분
* (6분)배열의 사이즈를 어떻게 처리하라는 부분을 빠트려서 추가함

* (17분) 정사각형에서 전치됐을때 처리

* (3분) 기존엔 초기조건이 잘 잡혔는데, 수정하면서 초기 조건 처리에 문제가 생김
* 해당 부분을 수정함

[시간 복잡도]
(연산횟수) * (정렬되는 행 또는 열의 수) * 정렬
100*100*100log(100)
대강 10**6 * 7

[반례] 처음부터 인덱스가 배열보다 큰 경우
1 12 4
1 2 3
4 5 6
7 8 9
답 : 20


r, c, k = map(int, input().split())
r, c = r-1, c-1
arr = [list(map(int, input().split())) for _ in range(3)]
ans = 0
t = 0   # 전치 여부를 저장

while ans!=101:

    if len(arr) > r and len(arr[0]) > c:
        if arr[r][c] == k: break

    ans += 1
    N, M = len(arr), len(arr[0])
    # 행이 무조건 더 짧거나 같게 전치
    # 다만 행과 열의 길이가 같을 때에는 전치 여부에 따라서
    # 또 전치를 할지 말지 결정해야함
    if N<M or (N==M and t):
        arr = list(zip(*arr))
        r, c = c, r
        t = 1-t

    lenth  = 0
    newarr = []
    for i in range(len(arr)):
        # 해당 숫자가 몇번 인덱스에 있는지
        dic = {}
        count = []
        for ele in arr[i]:
            # 0은 그냥 자리지기
            if ele==0: continue
            if ele not in dic:
                dic[ele]=len(count)
                count.append([ele, 0])
            count[dic[ele]][1]+=1

        count.sort(key = lambda x: (x[1], x[0]))
        # 새로운 행
        row = []
        for i in range(min(len(count), 50)):
            row.append(count[i][0])
            row.append(count[i][1])

        # 새로운 배열에 바뀐 행 넣기
        newarr.append(row)
        # 행들의 최대 길이 갱신
        lenth = max(lenth, len(row))

    # 행의 최대 길이보다 짧은 아이들은 0 추가하기
    for i in range(len(newarr)):
        while len(newarr[i])!=lenth:
            newarr[i].append(0)

    # 배열 갱신
    arr = newarr

if ans == 101: ans = -1
print(ans)
'''