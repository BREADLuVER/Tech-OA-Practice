from typing import List

def findNetworkCalls(reviews: List[int], counts: List[int]) -> List[int]:
    apicalls = 0

    for r in reviews:
        for c in counts:
            apicalls += (abs(r-c))

    return apicalls

reviews = [4, 6, 5, 2, 1]
counts = [3]
print(findNetworkCalls(reviews, counts))

reviews = [4, 6, 5, 2, 1]
counts = [3, 3, 3]
print(findNetworkCalls(reviews, counts))