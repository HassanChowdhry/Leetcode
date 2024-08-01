// https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_fuel = 0
        fuel = 0
        start = 0
        for i in range(n):
            total_fuel += gas[i]-cost[i]
            fuel += gas[i]-cost[i]

            if fuel < 0:
                fuel = 0
                start = i+1
        
        return start if total_fuel>=0 else -1

        print(take)
        return 0