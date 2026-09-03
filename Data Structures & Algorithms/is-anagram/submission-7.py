class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        length = len(s)
        s_bank = defaultdict(int)
        t_bank = defaultdict(int)
        for i in range(length):
            s_bank[s[i]] += 1
            t_bank[t[i]] += 1

        return s_bank == t_bank
