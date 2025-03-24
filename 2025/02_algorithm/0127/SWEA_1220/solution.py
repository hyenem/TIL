# 제출 횟수 : 1회
# 실행 시간 : 118ms
# 메모리 : 74,368 kb
# N극과 S극의 위치는 중요하지 않다고 판단했습니다.
# S극이 N극 밑에 연속해서 오는 경우를 세주었습니다.

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        flag = False
        pointer = 0
        if arr[pointer][i]==1:
            flag = True
        while pointer < 100:
            pointer+=1
            while pointer<100 and arr[pointer][i] != 2:
                if arr[pointer][i]==1:
                    flag = True
                pointer += 1
            if pointer==100:
                break
            if arr[pointer][i]==1:
                while pointer <100 and arr[pointer][i]!= 1:
                    pointer+=1
            if flag:
                ans += 1
                flag = False
    print(f'#{tc} {ans}')