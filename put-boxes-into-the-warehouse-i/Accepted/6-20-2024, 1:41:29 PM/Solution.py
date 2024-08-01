// https://leetcode.com/problems/put-boxes-into-the-warehouse-i

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes = sorted(boxes)
        stored = 0

        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i-1])
        
        right = len(warehouse)-1

        for box in boxes:
            while right >= 0 and box > warehouse[right]:
                right-=1
            if right < 0:
                return stored
            
            stored += 1
            right-=1
        
        return stored


