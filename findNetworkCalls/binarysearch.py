from typing import List
from bisect import bisect_left

def findNetworkCalls(reviews: List[int], counts: List[int]) -> List[int]:
    reviews.sort()
    prefix_sum = [0] * (len(reviews) + 1)

    for i in range(1, len(reviews) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + reviews[i - 1]

    result = []
    print(prefix_sum)

    for c in counts:
        idx = bisect_left(reviews, c)
        print(idx)
        
        left_cost = idx * c - prefix_sum[idx]
        print(left_cost)
        
        right_cost = (prefix_sum[-1] - prefix_sum[idx]) - (len(reviews) - idx) * c

        result.append(left_cost + right_cost)

    return result


reviews = [4, 6, 5, 2, 1]
counts = [3]
print(findNetworkCalls(reviews, counts))


# counts = [3, 5]
# print(findNetworkCalls(reviews, counts))
