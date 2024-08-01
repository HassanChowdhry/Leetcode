// https://leetcode.com/problems/sort-an-array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            n = len(nums)

            if n <= 1:
                return nums

            mid = n // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return merge(left, right)
        
        def merge(left, right):
            res = []
            l, r = len(left), len(right)
            i = j = 0

            while i < l and j < r:
                if left[i] < right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            if i < l: res += left[i:]
            if j < r: res += right[j:]

            return res
        
        return mergeSort(nums)