import collections
from typing import List

class Solution:
  def findMinimumVariance(self, height: List[int]) -> int:
    tracki = collections.defaultdict(list)
    tracko = collections.defaultdict(int)
    variance = float('inf')

    for i in range(len(height)):
      tracko[height[i]] += 1
      if height[i] not in tracki:
        tracki[height[i]] = i
      else:
        length = i - tracki[height[i]] + 1
        if length >= 2:
          variance = min(variance, length-tracko[height[i]])

    if variance == float('inf'):
      return -1
    return variance
    
solution = Solution()
print(solution.findMinimumVariance([4, 2, 5, 4]))
print(solution.findMinimumVariance([1, 2, 3, 4, 1]))
print(solution.findMinimumVariance([1, 2, 3, 4]))