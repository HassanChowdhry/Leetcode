// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:   
        min_num = nums[0]
        max_num = nums[0]
        res = [[min_num, max_num]]
        product = max_num

        for num in nums[1::]:
            prev_min = num*res[-1][0]
            prev_max = num*res[-1][1]
            
            min_num = min(num, prev_min, prev_max)
            max_num = max(num, prev_min, prev_max)
            res.append([min_num, max_num])

            product = max(product, max_num)
        
        return product