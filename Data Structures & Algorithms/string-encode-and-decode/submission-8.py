class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes, res = [], []

        # Storing the length of the items in sizes
        for item in strs:
            sizes.append(len(item))

        # Storing the lengths of each item in res in a string format
        for sz in sizes:
            res.append(str(sz))
            res.append(",")
        
        # Add delimeter
        res.append("#")
        # Add strs to the res
        res.extend(strs)

        # returns the encoded string in a string format
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        split_result = s.split('#', 1)
        num_split = split_result[0].rstrip(',').split(',')
        str_split = split_result[1]

        pos, res = 0, []
        for num in num_split:
            value = ''
            for i in range(int(num)):
                value += str_split[pos]
                pos += 1
            res.append(value)

        return res