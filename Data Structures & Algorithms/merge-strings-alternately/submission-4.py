class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Two-pointers approach

        i, j = 0, 0
        n, m = len(word1), len(word2)
        res = []

        while i < n or j < m:
            if i < n:
                res.append(word1[i])
            if j < m:
                res.append(word2[j])

            i += 1
            j += 1
        return ''.join(res)