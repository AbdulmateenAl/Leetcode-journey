class Solution:

    def encode(self, strs: List[str]) -> str:
        # If there is no strs return an empty string
        if not strs:
            return ""

        res = ''
        for word in strs:
            res += str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        # If there is no s return an empty list
        if not s:
            return []

        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length

            res.append(s[i:j])
            i = j

        return res