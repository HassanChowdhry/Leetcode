// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], w: List[int]) -> int:
        boxes = sorted(boxes, reverse=True)
        left, right = 0, len(w)-1
        stored = 0
        for box in boxes:
            if left > right:
                return stored
            
            if box > w[left] and box > w[right]:
                continue
            
            if w[left] > w[right]:
                left += 1
            else:
                right -=1
            
            stored += 1
        
        return stored
        
