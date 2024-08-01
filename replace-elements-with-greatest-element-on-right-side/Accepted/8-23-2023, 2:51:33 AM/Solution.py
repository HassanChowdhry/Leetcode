// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        num = -1
        temp = 0

        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = num
            num = max(temp, num)
        
        return arr