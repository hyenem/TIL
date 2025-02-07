_str = input()
bomb = input()
pointer = 0
stack = []
idx = []
for c in _str:
    if c==bomb[pointer]:
        if pointer+1 == len(bomb):
            for _ in range(pointer):
                stack.pop()
                idx.pop()
            if idx: pointer=idx[-1]
            else : pointer=0
            continue
        else :
            pointer+=1
    else :
        if c==bomb[0]:
            pointer =1
        else : pointer = 0
    stack.append(c)
    idx.append(pointer)
if stack : print(''.join(stack))
else : print('FRULA')
