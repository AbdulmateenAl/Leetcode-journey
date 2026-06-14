class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0
        count, maxf = {}, 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf <= k:
                res = max(res, (r - l + 1))
            else:
                count[s[l]] -= 1
                l += 1

            r += 1

        return res