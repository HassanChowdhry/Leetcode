// https://leetcode.com/problems/car-fleet

class Solution:
    def carFleet(self, target: int, positions: List[int], speed: List[int]) -> int:
        cars = len(positions)
        if cars == 1: return 1

        cars = [(positions[i], speed[i]) for i in range(cars)]

        pairs = sorted(cars, key=lambda x: x[0], reverse=True)
        stack = []

        for pos, sp in pairs:
            stack.append((target-pos) / sp)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)