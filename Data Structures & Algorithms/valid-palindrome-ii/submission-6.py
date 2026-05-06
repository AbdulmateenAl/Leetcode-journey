class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Using Two-pointer but with O(n) space
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                missingLeft = s[l + 1:r + 1]
                missingRight = s[l:r]
                return missingLeft == missingLeft[::-1] or missingRight == missingRight[::-1]
            
            l += 1
            r -= 1

        return True