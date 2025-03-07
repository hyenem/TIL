# solve1) dic 컴퓨터한테 시키기
arr =[list('qwertyuiop'), list('asdfghjkl'), list('zxcvbnm')]
dic = {}
# dic안에 해당 알파벳의 좌표 + 왼손(0), 오른손(1) 저장
for i in range(3):
    for j in range(len(arr[i])):
        if j < ((len(arr[i])+1)//2):
            dic[arr[i][j]]=(i,j,0)
        else :
            dic[arr[i][j]]=(i,j,1)

left, right = input().split()
hand = [[dic[left][0], dic[left][1]], [dic[right][0], dic[right][1]]]

ans = 0
for ele in list(input()):
    nx, ny, side = dic[ele]
    # 움직이는데 걸리는 시간 + 누르는데 걸리는시간(1)
    ans += abs(hand[side][0]-nx)+abs(hand[side][1]-ny)+1
    # 해당 손 좌표 바꿔주기
    hand[side][0]=nx
    hand[side][1]=ny
print(ans)


# solve2) 자음 모음 인덱스 맞추기
# 자음은 4이하로 , 모음은 5부터 시작하도록 인덱스 맞추기
l, r = input().split()
commands = input()
keyboard = {'q':(0,0), 'w':(0,1),'e':(0,2),'r':(0,3),'t':(0,4), 'y':(0,6), 'u':(0,7), 'i':(0,8), 'o':(0,9), 'p':(0,10),
        'a':(1,0), 's':(1,1),'d':(1,2),'f':(1,3),'g':(1,4), 'h':(1,6), 'j':(1,7), 'k':(1,8), 'l':(1,9),
        'z':(2,0), 'x':(2,1),'c':(2,2),'v':(2,3),'b':(2,5), 'n':(2,6), 'm':(2,7)}

ans = 0
lr, lc = keyboard[l] # 왼쪽 좌표
rr, rc = keyboard[r] # 오른쪽 좌표
for comm in commands:
    nr, nc = keyboard[comm]
    if nc <= 4: # 한글 자음(left)
        ans += (abs(lr - nr) + abs(lc - nc))
        lr, lc = nr, nc
    else:
        ans += (abs(rr - nr) + abs(rc - nc))
        rr, rc = nr, nc

# 이동 시간 + 각 키를 누르는데 걸리는 시간
print(ans+len(commands))