'''
제출횟수 : 1회
풀이시간 : 26분

메모리 : 122084KB -> 132640 KB
실행시간 : 296ms -> 244ms

! 명심할 것 !
* 이전에 사용한 인덱스를 for문의 인덱스로 사용하면 안되지!
* 인덱스 시작 0인지 1인지 확인할 것!

구상 : 6분
* 불의 정보를 어떻게 저장할 지 고민함
* 매 단계마다 전체 불을 다 보면서 좌표 겹치는 것 있는지 확인하는 것 보단
* 에초에 같은 좌표에 저장되게 하는게 좋겠다고 판단. arr와 narr를 2차원으로

* 범위 밖에 나가는 불이 어떻게 되는지 모르겠어서 한참 찾아봄
* 1행과 n행, 1열과 n열이 연결되어있다는 걸 확인하고 구현 시작

구현 : 12분
디버깅 : 8분
* merge하는 과정에서 한 칸에 한개있는 불도 옮겼어야했는데, 그렇지 않아서 수정

* M을 열 제한으로 생각해서 몇 가지를 N*N이 아니라 N*M으로 처리. 수정함

* 홀수 짝수 나눠서 새로운 방향을 추가해주는 과정에서 for 문 안에 i를 썼는데,
* 기존에 행으로 사용했던 i와 겹쳐져서 문제가 생김
* for문 안의 문자를 d로 변경

리팩토링
* merge 할 떄에만 좌표가 같은 아이들을 모아보면 되니까 arr는 같은 좌표끼리 모여있을 필요 없음
* arr를 1차원으로 변경
* 더불어 하나도 추가하지 않은 칸은 이중for문 돌면서 볼 필요 없으니까
* wheretomerge라는 set을 만들어서 불이 있는 칸만 봄


테스트 케이스
4 1 1
1 1 5 5 7
* 1행과 n행, 1열과 n열이 연결되어있다는 뜻을 해석하지 못한 경우
'''
dxdy = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
N, M, K = map(int, input().split())
arr = []
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    arr.append((x-1, y-1, m, s, d))

for _ in range(K):
    # 이동하기
    narr = [[[] for _ in range(N)] for _ in range(N)]
    # 합칠 때 봐야하는 좌표만 저장
    wheretomerge = set()
    while arr:
        x, y, m, s, d = arr.pop()
        # 1번행과 n번행, 1번 열과 n번열이 연결됨
        nx, ny = (x+dxdy[d][0]*s)%N, (y+dxdy[d][1]*s)%N
        narr[nx][ny].append((nx, ny, m, s, d))
        wheretomerge.add((nx, ny))


    # 합치기
    for i, j in wheretomerge:
        # 랍칠게 없이 1개만 있으면 다음단계에 그대로 전달
        if len(narr[i][j])==1:
            arr.append(narr[i][j][0])
            continue

        nm = 0
        ns = 0
        odd = 0
        even = 0
        for x, y, m, s, d in narr[i][j]:
            nm+=m
            ns+=s
            if d%2!=0:
                odd = 1
            else :
                even = 1
        nm = nm//5
        ns = ns//len(narr[i][j])
        if nm==0 : continue

        # 홀수인 경우와 짝수인 경우가 모두 있다면
        if even+odd ==2:
            for d in range(4):
                arr.append((i, j, nm, ns, d*2+1))
        # 그 외(둘 중 하나만 있다면)
        else :
            for d in range(4):
                arr.append((i, j, nm, ns, d*2))

ans = 0
for x, y, m, s, d in arr:
    ans += m

print(ans)