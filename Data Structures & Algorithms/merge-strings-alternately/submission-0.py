class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Brute-force solution
        max_length = len(word1) if len(word1) > len(word2) else len(word2)
        res = ''

        for i in range(max_length):
            if i < len(word1):
                res += word1[i]

            if i < len(word2):
                res += word2[i]

        return res