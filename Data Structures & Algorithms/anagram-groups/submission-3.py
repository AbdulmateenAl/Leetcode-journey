class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I think i know of two ways to solve this
        res = defaultdict(list)

        # First Method(Using sort)
        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     res[sorted_word].append(word)

        # Second Method
        for word in strs:
            alphabets = [0]*26
            for char in word:
                alphabets[ord(char) - ord("a")] += 1
            res[tuple(alphabets)].append(word)
        return list(res.values())