class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = [] # Stores an array of arrays
        pack = defaultdict(list)

        for word in strs:
            letters = [0] * 26 # Representation of the word in an array form
            for letter in word:
                letters[ord(letter) - ord('a')] += 1

            pack[tuple(letters)].append(word)

        for item in pack:
            result.append(pack[item])

        return result