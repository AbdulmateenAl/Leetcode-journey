class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Two-pointers approach

        first = 0
        second = 0
        max_length = len(word1) if len(word1) > len(word2) else len(word2)
        res = []

        while first < max_length or second < max_length:
            if first < len(word1):
                res.append(word1[first])
            if second < len(word2):
                res.append(word2[second])

            first += 1
            second += 1
        return ''.join(res)