def solution():
    arr = [0]+list(map(lambda x: int(x)-1, input().split()))
    if len(set(list(arr[1:5])))==1 and len(set(list(arr[9:13])))==1:
        if arr[13]==arr[14]==arr[7]==arr[8]:
            if arr[5]==arr[6]==arr[19]==arr[20]:
                if arr[17]==arr[18]==arr[23]==arr[24]:
                    if arr[21]==arr[22]==arr[15]==arr[16]:
                        print(1)
                        return
        elif arr[13]==arr[14]==arr[23]==arr[24]:
            if arr[5]==arr[6]==arr[15]==arr[16]:
                if arr[17]==arr[18]==arr[7]==arr[8]:
                    if arr[21]==arr[22]==arr[19]==arr[20]:
                        print(1)
                        return
        else :
            print(0)
            return
    elif len(set(list(arr[5:9])))==1 and len(set(list(arr[21:25])))==1:
        if arr[1]==arr[2]==arr[17]==arr[19]:
            if arr[18]==arr[20]==arr[9]==arr[10]:
                if arr[11]==arr[12]==arr[14]==arr[16]:
                    if arr[13]==arr[15]==arr[3]==arr[4]:
                        print(1)
                        return
        elif arr[1]==arr[2]==arr[14]==arr[16]:
            if arr[18]==arr[20]==arr[3]==arr[4]:
                if arr[11]==arr[12]==arr[17]==arr[19]:
                    if arr[13]==arr[15]==arr[9]==arr[10]:
                        print(1)
                        return
        else :
            print(0)
            return
    elif len(set(list(arr[13:17])))==1 and len(set(list(arr[17:21])))==1:
        if arr[1]==arr[3]==arr[6]==arr[8]:
            if arr[5]==arr[7]==arr[10]==arr[12]:
                if arr[9]==arr[11]==arr[21]==arr[23]:
                    if arr[2]==arr[4]==arr[22]==arr[24]:
                        print(1)
                        return
        elif arr[1]==arr[3]==arr[21]==arr[23]:
            if arr[5]==arr[7]==arr[2]==arr[4]:
                if arr[9]==arr[11]==arr[6]==arr[8]:
                    if arr[22]==arr[24]==arr[10]==arr[12]:
                        print(1)
                        return
        else :
            print(0)
            return
    print(0)
    return

solution()


