import sys

def syncopation():
    global starship_attack, star_power, over, change_over, alive
    if not over:
        ship[-1][1]+=star_power
        star_power = 0
        if ship and ship[-1][0] <= ship[-1][1] + sattack:
            h, a = ship.pop()
            acc[h] -= 1
            alive -= 1

        while ship and ship[-1][0] <= visited:
            h, a = ship.pop()
            if visited<h:
                acc[h]-=1
                alive -= 1

        change_over = 1
    else:
        star_power = 0
        starship_attack += 5
        over = 0

N = int(sys.stdin.readline().rstrip())
ship = list(map(lambda x: [int(x), 0], sys.stdin.readline().rstrip().split()))[::-1]
T = int(sys.stdin.readline().rstrip())
cmds = list(sys.stdin.readline().rstrip())
Q = int(sys.stdin.readline().rstrip())
question = list(map(int, sys.stdin.readline().rstrip().split()))

acc = [0]*1000002
visited = 0
for h, t in ship:
    acc[h]+=1

sattack = 0
star_power = 0
wish_cnt = 0
starship_attack = 0
over = 0
ans = [0]
alive = N
for cmd in cmds:

    star_power = min(1000000, star_power + 1 + (N-alive) + wish_cnt)
    if over:
        sattack += star_power//10
        if ship and ship[-1][0] <= ship[-1][1] + sattack:
            h, a = ship.pop()
            acc[h] -= 1
            alive -= 1

        while ship and ship[-1][0] <= max(visited, sattack):
            h, a = ship.pop()
            if visited < h:
                acc[h] -= 1
                alive -= 1

        if visited<sattack:
            alive -= sum(acc[max(visited, sattack-star_power//10)+1:sattack+1])
            visited = sattack
        starship_attack += star_power//10
        star_power = star_power%10

    change_over = 0

    if cmd=='W':
        pass

    elif cmd =='R':
        if star_power<3: pass
        else:
            heal_amount = min(3, starship_attack)
            star_power -= heal_amount
            starship_attack -= heal_amount

    elif cmd == 'P':
        if star_power<7: pass
        else:
            star_power -= 7
            wish_cnt += 1

    elif cmd == 'L':
        if not over:
            if star_power<5:
                syncopation()
            else:
                ship[-1][1]+=5
                star_power -= 5
                if ship[-1][0] <= ship[-1][1] + sattack:
                    h, a = ship.pop()
                    acc[h] -= 1
                    alive -= 1

                while ship and ship[-1][0] <= visited:
                    ship.pop()

        else :
            if star_power>=6:
                sattack += star_power
                if ship and ship[-1][0] <= ship[-1][1] + sattack:
                    h, a = ship.pop()
                    acc[h] -= 1
                    alive -= 1

                while ship and ship[-1][0] <= max(visited, sattack):
                    h, a = ship.pop()
                    if visited < h:
                        acc[h] -= 1
                        alive -= 1

                if visited<sattack:
                    alive -= sum(acc[max(visited, sattack-star_power)+1: sattack+1])
                    visited= sattack
                star_power = 0
            else:
                starship_attack += 5
                star_power = 0
            over = 0

    elif cmd == 'S':
        syncopation()

    if sattack:
        sattack -= 1
    else:
        if ship:
            if ship[-1][1]==0:
                starship_attack += alive
            else:
                ship[-1][1] -= 1
                starship_attack += alive-1


    ans.append((starship_attack, star_power, alive))

    if alive==0:
        break

    if change_over:
        over = 1

for t in question:
    if t>=len(ans):
        sys.stdout.write('skipped\n')
    else:
        a, b, c = ans[t]
        sys.stdout.write(f"{a} {b} {c}\n")