def findMaximumPackages(cost):
    from collections import defaultdict

    # Sort the array to make pairing predictable
    cost.sort()
    n = len(cost)
    max_packages = 0

    # Try every possible target sum from 2 * min(cost) to 2 * max(cost)
    for target_sum in range(2 * min(cost), 2 * max(cost) + 1):
        left, right = 0, n - 1
        current_packages = 0
        used = [False] * n  # Tracks whether an item is already paired

        # Use two-pointer approach to find pairs
        while left < right:
            if used[left]:  # Skip already paired items
                left += 1
                continue
            if used[right]:  # Skip already paired items
                right -= 1
                continue

            pair_sum = cost[left] + cost[right]
            if pair_sum == target_sum:
                # Valid pair
                current_packages += 1
                used[left] = used[right] = True
                left += 1
                right -= 1
            elif pair_sum < target_sum:
                left += 1  # Increase sum by moving left pointer
            else:
                right -= 1  # Decrease sum by moving right pointer

        # Update the maximum number of packages
        max_packages = max(max_packages, current_packages)

    return max_packages

# Test Cases
print(findMaximumPackages([4, 5, 10, 3, 1, 2, 2, 2, 3]))  # Output: 4
print(findMaximumPackages([1, 1, 2, 2, 1, 4]))            # Output: 3
print(findMaximumPackages([2, 1, 3]))                     # Output: 2
print(findMaximumPackages([10, 2, 1]))                    # Output: 1
