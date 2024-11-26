

def optimizeIdentifiers(s: str) -> int:
    target = s[0] + s[-1]

    def find(s, target, count):
        if len(s) < 1:
            return -1
        temp = s[0]+s[-1]
        if temp == target:
            return count
        
        remove_first = find(s[1:], target, count + 1)
        remove_last = find(s[:-1], target, count + 1)
        return max(remove_first, remove_last)
        
    return max(find(s[1:], target, 1), find(s[:-1], target, 1))

print(optimizeIdentifiers("babdcaac"))
print(optimizeIdentifiers("hchc"))