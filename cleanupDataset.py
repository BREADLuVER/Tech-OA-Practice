import collections

class Solution:
    def cleanupDataset(self, dataset: str, x: int, y: int) -> int:
        count = collections.Counter(dataset)
        ans = 0
        remain = 0

        if x <= y:
            for char in count:
                ans += (count[char] // 2) * x
                remain += count[char] % 2
        else:
            freq = list(count.values())
            while len(freq) > 1:
                freq.sort(reverse=True)
                a = freq.pop(0)
                b = freq.pop(0)
                pairs = min(a, b)
                ans += pairs * y
                a -= pairs
                b -= pairs
                if a > 0:
                    freq.append(a)
                if b > 0:
                    freq.append(b)
            
            for char_freq in freq:
                ans += (char_freq // 2) * x
                remain += char_freq % 2

        if remain > 0:
            ans += remain * y

        return ans


solution = Solution()
print(solution.cleanupDataset("abab", 2, 3))
print(solution.cleanupDataset("aaabca", 3, 2)) 
print(solution.cleanupDataset("aaaa", 3, 2)) 
print(solution.cleanupDataset("aaaa", 3, 5))
print(solution.cleanupDataset("aabbc", 2, 5)) 
