from typing import List
from collections import deque

def maximizeSimilarity(inv1: List[int], inv2: List[int]) -> int:
    n = len(inv1)
    deficit = deque()
    surplus = deque()
    operations = 0

    for i in range(n):
        diff = inv1[i] - inv2[i]
        if diff < 0:
            deficit.append((-diff, i))
        elif diff > 0:
            surplus.append((diff, i))

    print(f"Initial surplus: {surplus}")
    print(f"Initial deficit: {deficit}")

    while deficit and surplus:
        def_amt, def_idx = deficit.popleft() 
        sur_amt, sur_idx = surplus.popleft()

        transfer = min(def_amt, sur_amt)
        operations += transfer

        print(f"Transfer {transfer} from surplus index {sur_idx} to deficit index {def_idx}")
        
        def_amt -= transfer
        sur_amt -= transfer

        if def_amt > 0:
            deficit.appendleft((def_amt, def_idx))
        if sur_amt > 0:
            surplus.appendleft((sur_amt, sur_idx))

        print(f"Updated surplus: {surplus}")
        print(f"Updated deficit: {deficit}")
        print(f"Operations so far: {operations}")

    return operations


inv1 = [2, 4, 1] #[1,4,2], [1,3,3]
inv2 = [1, 2, 3]
print('operations: ', maximizeSimilarity(inv1, inv2)) # 2 operations
print()

inv1 = [2, 4, 1]
inv2 = [2, 4, 2]
print('operations: ', maximizeSimilarity(inv1, inv2)) # 0 operations
print()

inv1 = [1, 4, 2]
inv2 = [2, 4, 2]
print('operations: ', maximizeSimilarity(inv1, inv2)) # 0 operations
print()

#not working
inv1 = [2, 4, 1] #[3, 3, 1], [3, 2, 2]
inv2 = [3, 5, 2]
print('operations: ', maximizeSimilarity(inv1, inv2)) # 2 operations
print()

inv1 = [1, 2, 3] #[2, 2, 2], [2, 3, 1]
inv2 = [2, 4, 1]
print('operations: ', maximizeSimilarity(inv1, inv2)) # 2 operations