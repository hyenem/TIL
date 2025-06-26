def btk(n):
    s = n
    while s < 81:
        x, y = s//9, s%9
        if arr[x][y]!=0:
            s+=1
            continue
        for k in range(1, 10):
            if visited_row[x][k]: continue
            if visited_col[y][k]: continue
            if visited_box[(x//3)*3+y//3][k]: continue
            visited_row[x][k] = True
            visited_col[y][k] = True
            visited_box[(x // 3) * 3 + y // 3][k] = True
            arr[x][y]=k
            flag = btk(s+1)
            if flag: return True
            arr[x][y]=0
            visited_row[x][k] = False
            visited_col[y][k] = False
            visited_box[(x // 3) * 3 + y // 3][k] = False
        return False
    return True



visited_row = [[False]*10 for _ in range(9)]
visited_col = [[False]*10 for _ in range(9)]
visited_box = [[False]*10 for _ in range(9)]

arr = [list(map(int, input())) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if arr[i][j]!=0:
            visited_row[i][arr[i][j]]=True
            visited_col[j][arr[i][j]]=True
            visited_box[(i//3)*3+j//3][arr[i][j]]=True

btk(0)
for ele in arr:
    print(''.join(map(str, ele)))
