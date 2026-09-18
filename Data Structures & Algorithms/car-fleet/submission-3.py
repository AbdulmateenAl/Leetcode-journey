class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        
        fleet = 1
        highestTime = (target - pair[0][0]) / pair[0][1]

        for i in range(1, len(pair)):
            currentTime = (target - pair[i][0]) / pair[i][1]

            if currentTime > highestTime:
                fleet += 1
                highestTime = currentTime

        return fleet