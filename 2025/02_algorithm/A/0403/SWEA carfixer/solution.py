import heapq
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    A, B = A-1, B-1

    arr = [[0]*M for _ in range(N)]

    reception_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))
    people = list(enumerate(map(int, input().split())))
    people.sort(lambda x: (x[1], x[0]))

    reception_wait = []
    reception_shop_wait = []
    repair_wait = []
    reception = []
    for i in range(N):
        heapq.heappush(reception, (0, i))

    idx = 0
    time = 0
    while len(repair_wait)!=K:
        while idx!=K and people[idx][1]==time:
            heapq.heappush(reception_wait, people[idx])
            idx += 1

        while reception:
            rc_endtime, rc_idx = heapq.heappop(reception)
            if rc_endtime<=time:
                heapq.heappush(reception_shop_wait, (rc_idx, rc_endtime))
            else:
                heapq.heappush(reception, (rc_endtime, rc_idx))
                break

        while reception_wait and reception_shop_wait:
            rc_idx, rc_endtime = heapq.heappop(reception_shop_wait)
            p_idx, p_time = heapq.heappop(reception_wait)
            heapq.heappush(reception, (max(rc_endtime, p_time)+reception_time[rc_idx], rc_idx))
            repair_wait.append((max(rc_endtime, p_time)+reception_time[rc_idx], rc_idx, p_idx))

        time += 1




    repair_wait.sort()
    repair = []
    for i in range(M):
        heapq.heappush(repair, (0, i))

    idx = 0
    time = 0
    repair_shop_wait = []
    while idx!=K:
        while repair:
            rp_endtime, rp_idx = heapq.heappop(repair)
            if rp_endtime<=time:
                heapq.heappush(repair_shop_wait, (rp_idx, rp_endtime))
            else:
                heapq.heappush(repair, (rp_endtime, rp_idx))
                break

        while idx!=K and repair_wait[idx][0]<=time and repair_shop_wait:
            rp_idx, rp_endtime = heapq.heappop(repair_shop_wait)
            rc_end, rc_idx, p_idx = repair_wait[idx]
            arr[rc_idx][rp_idx] += p_idx + 1
            idx+=1
            heapq.heappush(repair, (max(rp_endtime, rc_end) + repair_time[rp_idx], rp_idx))

        time += 1

    print(f'#{tc} {arr[A][B] if arr[A][B] else -1}')