// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum([ abs(n1 - n2) for n1, n2 in zip(sorted(seats), sorted(students)) ])