// https://leetcode.com/problems/put-boxes-into-the-warehouse-i

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes = sorted(boxes, reverse=True)
        house = 0
        stored = 0
        for box in boxes:
            if house >= len(warehouse):
                break
            if box > warehouse[house]:
                continue
            house += 1
            stored += 1
        
        return stored


