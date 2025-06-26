'''
제출횟수 : 2회
    * 인덱스 에러
        -> 1*1 정사각형이 아니라 모든 정사각형이라고 생각하고 3중 for문을 작성하였는데,
        -> 출력 다시 읽고 마지막 for문을 지우는 과정에서
        -> 마지막 for문이 처리해줬을 index out of bound를 다시 처리해주지못함
풀이시간 : 28분

실행시간 : 108ms
메모리 : 111596KB




!! 명심할 것 1!!
혜민아,,,, 문제 이해하고 방법 떠올랐다고 일단 구현하지말고,,,
출력이 뭔지도 좀 제대로 읽자,,,,,제발,,,,,
>> 출력 오해하고 나중에 수정하면
>> 버그날 확률이 이만오천칠백퍼센트 상승

!! 명심할 것 2 !!
무언갈 수정하면,,, 그걸로 파생되는 다른 문제가 없는지 두고두고 확인할것,,,




[오해한 것]
>>첫째 줄에 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력한다.
>> '크기가 1x1'을 안읽었다,,,

* 수정 전 코드 : 오픈테케에서 걸림
    ans = 0
    for i in range(101):
        for j in range(101):
            if arr[i][j]==0: continue
            for k in range(1, 101-max(i, j)):
                if arr[i][j+k] and arr[i+k][j] and arr[i+k][j+k]:
                    ans += 1
    print(ans)

* 1차 수정 : 인덱스 에러
    ans = 0
    for i in range(101):
        for j in range(101):
            if arr[i][j]==0: continue
            if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
                    ans += 1
    print(ans)


구상 : 5분
* 드래곤 커브가 뭔지 이미 알고있어서, 내가 아는 개념이 맞는지 확인
* 드래곤 커브의 진행 방향 어떻게 구성할지 고민하고, 손 그림으로 검증

구현 : 8분
* 구현 과정에서 x, y를 나는 반대로 사용 하고 있던 것을 깨닫고 바꿔서 받음

디버깅 : 13분
* 배열 찍어서 드래곤 커브 잘 그려지는지 확인하고
* 출력을 잘못 이해한건데, x, y 좌표 바뀐 것 때문인 줄 알고, 애먼 좌표만 계속 바꿔봄
* 내가 생각하는 출력과 예제의 출력이 다르다는걸깨닫는데까지 12분,,,,,,,
* 그 이후 1분만에 수정하고 제출 -> 해서 인덱스에러^^^^^^^

[시간 복잡도]
N*(2**g)+10000

[엣지케이스] : 모든 드래곤 커브가 겹치는 경우
4
3 3 0 1
3 3 0 1
3 3 0 1
3 3 0 1


'''


N = int(input())
arr = [[0]*101 for _ in range(101)]
dxdy = ((0, 1), (-1, 0), (0, -1), (1, 0))

# 0 번으로 시작할 때의 드래곤 커브 만들어놓기
direction = [0]
for _ in range(10):
    # 뒤에서 부터 보면서 모든 진행 시계방향으로 90도씩 바꿔서 더해주기
    # 시장에 가면 거꾸로 하는 느낌쓰~
    idx = len(direction)-1
    while idx>=0:
        direction.append((direction[idx]+1)%4)
        idx -= 1

for _ in range(N):
    y, x, d, g = map(int, input().split())
    arr[x][y]=1

    # 그 길 따라 가면서 표시하기
    for i in range(2**g):
        dx, dy = dxdy[(direction[i]+d)%4]
        x += dx
        y += dy
        arr[x][y]=1

ans = 0
for i in range(100):
    for j in range(100):
        # 정사각형이 다 1이면 정답 늘리기
        if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
                ans += 1
print(ans)