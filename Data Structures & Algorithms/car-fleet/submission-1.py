class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        result = defaultdict(list)
        pair.sort(reverse=True)
        fleet = -float('inf')

        for p,s in pair:
            distance = target - p
            time = distance / s

            fleet = max(fleet, time)
            result[fleet].append(p)

        return len(result)