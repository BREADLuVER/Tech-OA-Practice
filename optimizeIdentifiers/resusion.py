

def optimizeIdentifiers(s: str) -> int:
    if not s:
        return 0
    elif len(s) == 1:
        return 0
    
    target = s[0] + s[-1]

    def find(s, target, count):
        if len(s) < 1:
            return 0
        temp = s[0]+s[-1]
        if temp == target:
            return count
        
        remove_first = find(s[1:], target, count + 1)
        remove_last = find(s[:-1], target, count + 1)
        return max(remove_first, remove_last)
        
    return find(s[1:], target, 1)

print(optimizeIdentifiers("babdcaac"))
print(optimizeIdentifiers("hchc"))
print(optimizeIdentifiers("h"))
print(optimizeIdentifiers(""))