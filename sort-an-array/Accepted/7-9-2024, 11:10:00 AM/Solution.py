// https://leetcode.com/problems/sort-an-array

from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            res = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            
            if i < len(left): res += left[i:]
            if j < len(right): res += right[j:]

            return res


        def mergeSort(nums: List[int]) -> List[int]:
            n = len(nums)
            if n <= 1:
                return nums
            
            middle = n//2
            left = nums[:middle]
            right = nums[middle:]

            left = mergeSort(left)
            right = mergeSort(right)
            
            return merge(left, right)
        
        return mergeSort(nums)