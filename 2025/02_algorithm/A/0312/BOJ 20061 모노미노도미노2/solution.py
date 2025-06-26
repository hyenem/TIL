'''
풀이시간 : 52분
제출횟수 : 3회
    # 위에 넘치는 만큼 터트리기 로직이 잘봇됨
        # pop을 처음엔 fall<2 일 때, 2-fall 만큼 함
        # -> fall이 1또는 2인 경우 H-fall+1만큼 해야하니까 당연히 틀렸습니다

        # 그리고 나서  fall이 1또는 2인 경우 H-fall+1만큼으로 수정
        # 점수를 얻고나면 행이 없어지니까 ㅠ 흐린 부분도 아래로 한칸씩 내려가는데
        # fall을 그대로 사용하면 반영을 못함 ㅠ -> 틀렸습니다

        # 결국 갱신 이후 다시 확인해주는 로직으로 바꿈

실행시간 : 212ms
메모리 : 114464KB

[시간 복잡도]
아아아아아ㅏ아무리커도 64*N은 안넘지 않을까?

[엣지 케이스] : 넘쳤는데, 점수가 추가돼서 안넘치게 되는 경우
7
2 0 0
3 0 0
2 0 1
2 0 2
2 0 1
1 0 3
3 0 0

!! 명심할 것 !!
틀렸습니다를 보면 주로 어디가 틀렸는지는 바로 아는데,
그 부분을 수정하고 맞을거라고 확신하는 경향이 있음
내 머릿속에서 로직이 완벽하더라도 이전에 틀린 이유 반례 만들어서 무조건 돌려보기

구상 : 8분
* 결국은 초록이랑 파랑이 저런 모양으로 있을 이유가 없고
* 빨강의 열에 초록이 영향을 받고
* 빨강의 행에 파랑이 영향을 받는다고 생각해서
* 각각을 쪼개서 처리하기로함
* 더불어서 한줄이 터지는 작업은 전체 좌표를 다 옮기는 거보다
* 그냥 행에 참조값 삭제하고 새로운 행 추가하는게 더 빠르지 않을까? 라는 생각
* 그래서 행을 지우고 0번 인덱스에 새로운 행을 추가하기로함

구현 : 28분
* 일단 초록색 만들어놓고 잘 돌아가는지 확인함
* 그리고 파랑 복붙

디버깅 : 16분
* 넘치는 부분 팝하는데에서 1+fall만큼 팝하게 했는데, openTC 안맞음
* 2-fall 만큼 팜하게 하니까 맞았음
* 그리고 틀렸습니다,,,,,,,,
* 위에 적어둔 틀렸습니다 이유 파악하고, 고치는데 남은 시간 사용

리팩토링
* 문제 풀면서도 초록이랑 파랑이 똑같이 돌아간다고 생각했지만
* 일단 복붙해서 제출하기로함
* 같은 로직 함수로 뽑아서 처리함

'''


def drop(arr, W, H):
    global ans

    # 어디까지 떨어트릴 수 있는지 계산
    fall = 0
    for i in range(2, 6):
        for c in W:
            if arr[i][c]:
                fall = i - 1
                break
        if fall: break
    else:
        fall = 5

    # 떨어트리기
    for c in W:
        for h in range(H):
            arr[fall - h][c] = 1

    # 점수 올릴 수 있으면 올리기
    for h in range(H - 1, -1, -1):
        if sum(arr[fall - h]) == 4:
            ans += 1
            del arr[fall - h]
            arr.insert(0, [0, 0, 0, 0])

    # 위에 넘치는 만큼 터트리기
    # 여기서 pop을 처음엔 fall<2 일 때, fall+1 만큼 함
    # -> fall이 1또는 2인 경우 H-fall+1만큼 해야하니까 당연히 틀렸습니다

    # 그리고 나서  fall이 1또는 2인 경우 H-fall+1만큼으로 수정
    # 점수를 얻고나면 행이 없어지니까 ㅠ 흐린 부분도 아래로 한칸씩 내려가는데
    # fall을 그대로 사용하면 반영을 못함 ㅠ -> 틀렸습니다

    # 결국 갱신 이후 다시 확인해주는 로직으로 바꿈

    # 그런데 사실, 점수를 얻고 나서 넘치는 건 불가능하다
    # 그래서 이전 로직에서 점수를 얻었으면 그냥 return 하도록 만들었으면 안틀렸을듯
    pop = 0
    if sum(arr[0]) != 0:
        pop = 2
    elif sum(arr[1]) != 0:
        pop = 1
    for _ in range(pop):
        arr.pop()
        arr.insert(0, [0, 0, 0, 0])


green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]

ans = 0
N = int(input())
blocks = [tuple(map(int, input().split())) for _ in range(N)]

for t, x, y in blocks:
    # 각 블럭에 대해서 파란칸과 초록칸에
    # 블럭이 떨어질 열과 높이를 계산
    greenh = 1
    blueh = 1
    if t == 1:
        greenw = (y,)
        bluew = (x,)
    elif t == 2:
        greenw = (y, y + 1)
        bluew = (x,)
        blueh = 2
    else:
        greenw = (y,)
        greenh = 2
        bluew = (x, x + 1)

    drop(green, greenw, greenh)
    drop(blue, bluew, blueh)

print(ans)
ans2 = sum(map(sum, green)) + sum(map(sum, blue))
print(ans2)

