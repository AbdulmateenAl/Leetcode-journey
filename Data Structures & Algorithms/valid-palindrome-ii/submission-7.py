class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Using Two-pointer but with O(1) space

        # This function checks if the sub-string is a palindrome
        def isPalindrome(l: str, r: str):
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)

            l += 1
            r -= 1

        return True