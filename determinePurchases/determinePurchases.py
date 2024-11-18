import heapq
from collections import deque

def purchaseVolumes(volumes):
    n = len(volumes)
    heap = []
    max_owned = 0
    result = []

    for day in range(n):

        heapq.heappush(heap, volumes[day])

        print(heap)

        purchased_today = []

        while heap and heap[0] == max_owned + 1:
            next_volume = heapq.heappop(heap)
            purchased_today.append(next_volume)
            max_owned += 1

        if purchased_today:
            result.append(purchased_today)
        else:
            result.append([-1])

    return result


volumes = [2, 1, 4, 3]
print(purchaseVolumes(volumes))