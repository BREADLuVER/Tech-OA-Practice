class Solution:
    def isSpecialSequence(self, dna_sequence: str) -> str:
        def can_form_palindrome(s, removal_allowed=True):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    if not removal_allowed:
                        return False
                    return can_form_palindrome(s[left + 1:right + 1], False) or \
                           can_form_palindrome(s[left:right], False)
                left += 1
                right -= 1
            return True
            
        for i in range(1, len(dna_sequence)):
            left_part = dna_sequence[:i]
            right_part = dna_sequence[i:]
            
            if can_form_palindrome(left_part) and can_form_palindrome(right_part, False):
                return "YES"
            if can_form_palindrome(left_part, False) and can_form_palindrome(right_part):
                return "YES"

        return "NO"


solution = Solution()
print(solution.isSpecialSequence("abcad"))
print(solution.isSpecialSequence("abcd"))
print(solution.isSpecialSequence("abcdabad"))
print(solution.isSpecialSequence("ab"))
