class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        total = 0
        index = 0

        for i in range(len(gas)):
            tank += (gas[i] - cost[i])
            total += (gas[i] - cost[i])

            if tank < 0:
                tank = 0
                index = i + 1
        if total >= 0:
            return index
        else:
            return -1

        
