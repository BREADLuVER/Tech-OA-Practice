from collections import Counter
import heapq

class Solution:
    def findMinimumTimeRequired(self, requests: str, minGap: int) -> int:
        freq = Counter(requests)

        max_heap = [(-count, region) for region, count in freq.items()]
        heapq.heapify(max_heap)
        print('max_heap:', max_heap)

        cooldown = {}
        time = 0
        while max_heap or cooldown:
            time += 1
            
            if time in cooldown:
                heapq.heappush(max_heap, cooldown.pop(time))
            
            if max_heap:
                count, region = heapq.heappop(max_heap)
                count = -count

                count -= 1

                if count > 0:
                    cooldown[time + minGap + 1] = (-count, region)
        
        return time


solution = Solution()
print(solution.findMinimumTimeRequired("abacadaeafag", 2))  # Output: 16
print(solution.findMinimumTimeRequired("aaabbb", 0))        # Output: 6
print(solution.findMinimumTimeRequired("aaabbb", 2))        # Output: 8