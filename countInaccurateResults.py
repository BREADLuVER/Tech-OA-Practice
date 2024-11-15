import collections
from typing import List

class Solution:
    def countInaccurateResults(self, processOrder: List[int], executionOrder: List[int]) -> int:
        track = {k: i for i,k in enumerate(processOrder)}
        inaccurate = 0
        executed = set()

        for p in executionOrder:
            curr_pos = track[p]
            for i in range(curr_pos):
                if processOrder[i] not in executed:
                    inaccurate += 1
                    break
            executed.add(p)

        return inaccurate

solution = Solution()
print(solution.countInaccurateResults([2, 3, 5, 1, 4], [5, 2, 3, 4, 1]))
print(solution.countInaccurateResults([4,1,2,3], [1,2,3,4]))
print(solution.countInaccurateResults([2, 3, 5, 1, 4], [2, 5, 3, 4, 1]))